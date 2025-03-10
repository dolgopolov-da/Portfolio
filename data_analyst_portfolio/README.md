# Projects
____________________________________________________________________________________________________
## 1. Парсер информации по рынку недвижимости

Парсер объявлений о продаже недвижимости.
Проход по страницам с объявлениями из поиска, сохранение кода страниц в файл.
Парсинг кода страниц, сохранение данных из объявлений в csv таблицы.

### Usage

*Использованные загружаемые бибилиотеки*
Beautiful soup, selenium, webdriver_manager, pandas

*Run*
- main file: "Parser_avito_main_v.2.py"
- urls list: "avito_urls.py"
- csv to google sheets: "csv_to_google_sheets.py"
- and service files

____________________________________________________________________________________________________
## 2. Дашборд для визуализации данных по рынку недвижимости
Отображение данных из csv таблиц, полученных парсером, в удобном формате дашборда на Yandex DataLens
Ссылка на дашборд: https://datalens.yandex.ru/ivkbx3xexkmg8-avito-nedvizhimost

____________________________________________________________________________________________________
## 3. Разное
В этом каталоге представлены прочие проекты, выполненные в период проектной деятельности и обучения

### 3.1. Euler project
Некоторые решенные задачи с ресурса "Проект Эйлера" https://euler.jakumo.org/problems.html

### 3.2. Stepic
Некоторые решенные задачи с пройденных на платформе Stepic курсов

### 3.3. Karpov.courses
Промежуточный и финальный проекты с курса от Karpov.courses по специализации "Аналитик данных"

**Задачи, решенные в промежуточном проекте (e-commerce):**
- по имеющимся данным - проанализировал совершенные покупки и ответил на поставленные руководством вопросы:
  * определили количество пользователей, которые совершили покупку только один раз
  * определил, сколько заказов в месяц в среднем не доставляется по разным причинам (вывел детализацию по причинам)
  * по каждому товару определил, в какой день недели товар чаще всего покупается
  * определил, сколько у каждого из пользователей в среднем покупок в неделю (по месяцам)
- провел когортный анализ пользователей, используя pandas. В период с января по декабрь выявил когорту с самым высоким retention на 3й месяц
- используя python, построил RFM-сегментацию пользователей

**Задачи, решенные в финальном проекте (A/B-тестирование, SQL, python):**
- провел A/B-тестирование с целью проанализировать итоги эксперимента
- составил несколько SQL-запросов (от простого к более сложному) в соответствии с заданием
- написал python скрипт для автоматизации подгрузки доп. данных эксперимента и построения графиков по получаемым метрикам 

### 3.4. Mailer Flask
Прием данных с формы корзины на сайте, обработка POST запроса, формирование письма о заказе на почту магазина и покупателя

### 3.5. CSV_to_JSON converter
Конвертор каталога товаров магазина из таблицы в формате CSV в формат JSON для автоматической загрузки товаров на сайт магазина

___________________________________________________________________________________________________________________________________
## 5. Визуализация ежемесячных расходов
Выгрузка данных по ежемесячным тратам из GSpreadsheet в датафрейм, обработка и обратная загрузка в GS в удобный для Yandex DataLens формат. Построение дашборда

___________________________________________________________________________________________________________________________________
## 6. Парсер информации по рынку земельных участков
Парсер объявлений о продаже земельных участков.
Проход по страницам с объявлениями из поиска, сохранение кода страниц в файл.
Парсинг кода страниц, сохранение данных из объявлений в csv таблицы.
Загрузка итоговой таблицы в GSpreadSheet, построение дашборда в Yandex DataLens
Ссылка на дашборд: https://datalens.yandex.ru/kkktuvut8v1m9-avito-zu

___________________________________________________________________________________________________________________________________
## 7. Интерактивная карта по рынку земельных участков Ленинградской области
Ссылка на дашборд: https://datalens.yandex.cloud/u5g0j99a0kqmh

___________________________________________________________________________________________________________________________________
## 8. Интерактивная карта с лотами на муниципальных торгах
Ссылка на дашборд: https://datalens.yandex/b4fbytg7f3mqz

___________________________________________________________________________________________________________________________________
## 9. Веб-приложение с отображением лотов на муниципальных торгах и объявлений с авито на интерактивной карте
