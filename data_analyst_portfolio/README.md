# Projects

## 1. Avito_parser

Парсер объявлений о продаже недвижимости.
Проход по страницам с объявлениями из поиска, сохранение кода страниц в файл.
Парсинг кода страниц, сохранение данных из объявлений в csv таблицы.


### Usage

*Setup*
- Скопировать каталог "1_avito_parsing"
- pip install bs4
- pip install selenium
- pip install webdriver_manager
- pip install pandas

*Run*
- main file: "Parser_avito_main_v.2.py"
- urls list: "avito_urls.py"
- csv to google sheets: "csv_to_google_sheets.py"
- and service files

Pages code and .csv files saves to dir "flats_from_avito"


## 2. Dashboard in DataLens
Отображение данных из csv таблиц, полученных парсером, в удобном формате дашборда на Yandex DataLens
Ссылка на дашборд: https://datalens.yandex.ru/ivkbx3xexkmg8-avito-nedvizhimost

## 3. Different tasks
В этом каталоге представлены прочие проекты, выполненные в период обучения

### 3.1. Euler project
Некоторые решенные задачи с ресурса "Проект Эйлера" https://euler.jakumo.org/problems.html

### 3.2. Stepic
Некоторые решенные задачи с пройденных на платформе Stepic курсов

### 3.3. Karpov.courses
Промежуточный и финальный проекты с курса от Karpov.courses по специализации "Аналитик данных"

### 3.4. Mailer Flask
Прием данных с формы корзины на сайте, обработка POST запроса, формирование письма о заказе на почту магазина и покупателя

### 3.5. CSV_to_JSON converter
Конвертор каталога товаров магазина из таблицы в формате CSV в формат JSON для автоматической загрузки товаров на сайт магазина
