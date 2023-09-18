from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
import os
import re
import pandas as pd
from urls.avito_urls import *


def get_data(url, headless=True, sleep_time=10):
    """Функция создает драйвер, подключается к заданному url, записывает в файл код страницы и возвращает название
    этого файла"""
    'задаем переменную с опциями драйвера'
    service = Service(ChromeDriverManager().install())
    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument('--disable-blink-features=AutomationControlled')  # disable webdriver mode
    if headless:
        webdriver_options.add_argument('--headless')  # фоновый режим работы браузера ! отключить, если не нужно
    driver = webdriver.Chrome(service=service, options=webdriver_options)

    file_path, pages_number = '', 1  # костыль, чтобы убрать local variable might be referenced before assignment
    'ЗАПУСКАЕМ драйвер и создаем текстовый файл для записи в него кода страниц'
    try:
        start_parsing_url = time.time()

        'проверка существования директории с файлами кода страниц'
        if not os.path.isdir('page_code/'):
            os.mkdir('page_code/')
        file_path: str = 'page_code/page_code.txt'

        """Для прохода по всем страницам создадим цикл, на каждой итерации будем менять значение переменной url на 
        новое, соответствующее адресу каждой последующей страницы """
        'получаем количество страниц в поисковой выдаче'
        pages_number = number_of_pages(file_path)
        print(f'Количество страниц: {pages_number}')

        for page in range(1, pages_number + 1):
            print(f'Парсинг {page} страницы...', end='')

            'получаем и записываем код страницы в файл'
            driver.get(url=url + f'?p={page}')
            time.sleep(sleep_time)
            if page == 1:
                with open(file_path, 'w') as f:
                    f.write(f'''\n\n\n<<< Страница {page} >>>\n\n\n''')
                    f.write(driver.page_source)
            else:
                with open(file_path, 'a') as f:
                    f.write(f'''\n\n\n<<< Страница {page} >>>\n\n\n''')
                    f.write(driver.page_source)
            print(f'''завершено.''')

        end_parsing_url = time.time() - start_parsing_url
        print(f'Время сбора кода страниц: {int(end_parsing_url)} сек.')
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        return file_path, pages_number  # возвращаем путь к текстовому файлу с кодом страниц и кол-во страниц


def number_of_pages(file_path):
    """Функция возвращает количество страниц, с которых нужно собрать информацию:
       парсит цифру с первой страницы поиска"""
    with open(file_path) as file:
        page_code = file.read()
    soup = BeautifulSoup(page_code, 'html.parser')
    pagination_div = soup.find('div', class_='js-pages pagination-pagination-_FSNE')
    pagination_spans = pagination_div.find_all('span', class_='styles-module-text-InivV')
    pages_number = int(pagination_spans[-1].get_text())

    return pages_number


def get_item_parameters(file_path):
    with open(file_path) as file:
        page_code = file.read()

    soup = BeautifulSoup(page_code, 'html.parser')
    item_divs = soup.find_all('div', class_='iva-item-body-KLUuy')

    'Delete ad_divs (рекламные) from item_divs'
    del_items = []
    for i in range(len(item_divs)):
        if item_divs[i].find('div', class_='geo-root-zPwRk') is None:
            del_items.append(i)
    for i in del_items[::-1]:
        del item_divs[i]

    'Create lists of parameters'
    urls = []
    prices = []
    squares = []
    types = []
    dates_days = []
    dates_text = []
    addresses = []

    for item in item_divs:
        '1. URL'
        item_url = item.find('div', class_='iva-item-title-py3i_').find('a').get('href')

        '2. Price'
        item_price = item.find('div', class_='price-price-JP7qe') \
            .find('meta', itemprop="price") \
            .get('content')

        '3. Square, type'
        item_name = item.find('div', class_='iva-item-title-py3i_') \
                        .find('h3') \
                        .get_text().split()
        # print(item_name)
        if len(item_name) > 1:
            if 'га' in item_name[2].lower() and (re.match(r'^\d+,\d+$', item_name[1])
                                                 or re.match(r'^\d+$', item_name[1])):
                item_square = float(item_name[1].replace(',', '.')) * 100
            elif 'сот' in item_name[2].lower() and (re.match(r'^\d+,\d+$', item_name[1])
                                                    or re.match(r'^\d+$', item_name[1])):
                item_square = float(item_name[1].replace(',', '.'))
            else:
                item_square = f'{item_name[1].replace(",", ".")} {item_name[2].lower()}'
        else:
            item_square = 0  # отсекаем объявления без указания площади участка

        if re.search(r'\((\w+,*\s*\w*)\)', ' '.join(item_name)):
            item_type = re.search(r'\((\w+,*\s*\w*)\)', ' '.join(item_name)).group(1)
        else:
            item_type = ''

        '4. Date'
        item_date_text = item.find('div', class_='iva-item-dateInfoStep-_acjp').find('p').get_text()
        item_date_day = convert_to_normal_date(item_date_text)
        date_pattern = r'(\d{1,2})\s(\w+)\s\d{1,2}:\d{1,2}'
        re_result = re.findall(date_pattern, item_date_day)
        if re_result:
            # print(item_date_day)
            # print(re_result)
            item_day = re_result[0][0]
            item_month = re_result[0][1]
            item_year = datetime.date.today().year
            item_date_day = f'{item_day}.{item_month}.{item_year}'

        '5. Address'
        item_address = item.find('div', class_='geo-root-zPwRk') \
                           .find('span')\
                           .get_text()

        '6. ADD to lists'
        urls.append('https://www.avito.ru' + item_url)
        prices.append(int(item_price))
        squares.append(item_square)
        types.append(item_type)
        dates_days.append(item_date_day)
        dates_text.append(item_date_text)
        addresses.append(item_address)

    return urls, prices, squares, types, dates_days, dates_text, addresses


def convert_to_normal_date(date):
    """Функция для конвертации даты типа '2 часа/дня/минуты назад' в дату нужного формата '20.09.2022'.
       Применяется внутри функции get_item_parameters()"""

    if any(substr in date for substr in ['день', 'дня', 'дней']):
        days_back = float(date.split()[0])
        normal_date = (datetime.datetime.today() - datetime.timedelta(days=days_back)).strftime('%d.%m.%Y')
        return normal_date
    elif 'час' in date or 'минут' in date:
        normal_date = (datetime.datetime.today()).strftime('%d.%m.%Y')
        return normal_date
    elif 'недел' in date:
        weeks_back = float(date.split()[0])
        normal_date = (datetime.datetime.today() - datetime.timedelta(weeks=weeks_back)).strftime('%d.%m.%Y')
        return normal_date
    else:
        return date


def main():
    """Запускаем цикл для итерации по списку ссылок на объявления в разных регионах"""
    for region, url in zip(list(url_dict.keys()), list(url_dict.values())):  # url + "?p=1"
        print(f'Начинаю парсинг объявлений в регионе: {region}')

        while True:
            answer = input('Нужно ли парсить код страниц поисковой выдачи? (да/нет): ')
            if answer.lower() in ('да', 'нет'):
                break
            else:
                print('Выберите из предложенных вариантов (да/нет).')

        if answer == 'да':
            """1. Блок сбора кода страниц; для отмены фонового режима установить параметр headless=False"""
            file_path, pages_number = get_data(url=url, headless=True, sleep_time=10)  # True - запуск в фоновом режиме
            print(f'Файл записан в {file_path}')
        else:
            """Блок для корректировки дальнейшей работы функции, без повторных обращений к сайту 
              (когда код страниц уже есть: например, функция get_data отработала без ошибок, а при сборе параметров 
              ошибка)"""
            if not os.path.isdir('page_code/'):
                os.mkdir('page_code/')
            file_path = 'page_code/page_code.txt'
            pages_number = number_of_pages(file_path)
            print(f'Количество страниц: {pages_number}')

        "3. Формирование списков с данными по объявлениям"
        start_parsing_soup = time.time()
        urls, prices, squares, types, dates_days, dates_text, addresses = get_item_parameters(file_path)
        end_parsing_soup = time.time() - start_parsing_soup

        print(f'''Время сбора конкретных данных из кода страниц: {int(end_parsing_soup)} сек., в среднем на каждое 
                          объявление - {int(end_parsing_soup / len(urls))} сек.''')

        print(f'''С {pages_number} страниц собрана информация по следующему количеству объявлений:
                - url: {len(urls)}
                - цены: {len(prices)}
                - тип: {len(types)}
                - площадь: {len(squares)}
                - адрес: {len(addresses)}
                - дата объявления: {len(dates_days)}
                - дата, примечание: {len(dates_text)}
                ''')

        "4. Формирование итогового датафрейма и сохранение его в .csv/xlsx"
        total_df = pd.DataFrame({'Ссылка': urls,
                                 'Стоимость': prices,
                                 'Тип участка': types,
                                 'Площадь в сотках': squares,
                                 'Стоимость 1 сотки': [int(x / a) if isinstance(a, float) else ''
                                                       if a != 0 else 0  # отсекаем объявления без указания площади
                                                       for x, a in zip(prices, squares)],
                                 'Адрес': addresses,
                                 'Дата': dates_days,
                                 'Дата прим.': dates_text})

        if not os.path.exists('landplots'):
            os.mkdir('landplots')
        if not os.path.exists(folder_path_monthly):
            os.mkdir(folder_path_monthly)
            os.mkdir(folder_path_daily)
        elif not os.path.exists(folder_path_daily):
            os.mkdir(folder_path_daily)
        total_df.to_csv(f'{folder_path_daily}/landplots_{today_date}.csv')

        print(f'Таблица с объявлениями в регионе: {region} записана в размере {len(urls)} строк')
        print(f'Файл с таблице сохранен в каталоге {os.path.abspath(folder_path_daily)}')


if __name__ == "__main__":
    start = time.time()

    "Объявляем временные переменные и пути для сохранения файлов"
    month = datetime.datetime.today().strftime('%Y.%m')
    today_date = datetime.datetime.today().strftime('%Y.%m.%d')
    folder_path_monthly = f'landplots/adds_by_{month}'
    folder_path_daily = f'landplots/adds_by_{month}/{today_date}'

    """Запускаем основную функцию"""
    main()

    """Если нужно, запускаем функцию склеивания таблиц. Можно запустить отдельно, без запуска main."""
    # concat_tables(folder_path_daily, today_date)

    end = time.time() - start
    print(f'Время выполнения программы: {int(end)} сек.')
