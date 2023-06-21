#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import json
import numpy as np

price = pd.read_csv('price.csv', sep=';', encoding='windows-1251')

price.head(2)

price = price.rename(columns={'Артикул' : '_id', 'Категория' : 'category',                               'Наименование, харак-ка' : 'title',                               'количество штук в упаковке' : 'value',                               'цена за упаковку' : 'price', 'Видео' : 'link',                               'В наличии' : 'hide'})

for i in price.columns:
    if i.startswith('Unnamed'):
        price = price.drop(columns=[i])

price = price.dropna()

if type(price.value[0]) == str:
    price.value = price.value.str.rstrip('.').str.rstrip(' шт').astype('int')

if price.price.dtypes == 'object':
    price.price = price.price.str.replace(',', '.').astype('float')
elif price.price.dtypes == 'int64':
    price.price = price.price.astype('float')

price.category = price.category.str.rstrip(' ').str.rstrip('.')

price.title = price.title.str.replace('\n', ' ')

for i in range(len(price.index)):
    if price.loc[i, 'hide'] == 0:
        price.loc[i, 'hide'] = True
    else:
        price.loc[i, 'hide'] = False

price = price.fillna('')

price.title = price._id + ' ' + price.title
price_columns = price.columns

# add categories for json
categories = [{"title": "Все", "value": "all"}]
used_categories = []
for i in price.index:
    category = {}
    if price.loc[i, 'category'] not in used_categories:
        category["title"] = price.loc[i,'category']
        category["value"] = price.loc[i,'category'] #FIX!
        used_categories.append(price.loc[i,'category'])
        categories.append(category)

for i in categories:
    if i['title'] == 'Хлопушки. Начинка, длина':
        i['title'] = 'Хлопушки'
    elif i['title'] == 'Пневмохлопушки. Начинка, длина':
        i['title'] = 'Пневмохлопушки'
    elif i['title'] == 'Римские свечи (калибр х колич.выстрелов)':
        i['title'] = 'Римские свечи'
    elif i['title'] == 'Одиночные салюты, фестивальные шары. (калибр " Х колич шаров)':
        i['title'] = 'Одиночные салюты, фестивальные шары'
    elif i['title'] == 'Батареи салютов  (калибр Х колич. стволов)':
        i['title'] = 'Батареи салютов'


# add items for json
items = []
for i in range(len(price.index)):
    item = {}
    price_row = price.loc[i,:].to_list()
    for j in range(len(price_columns)):
        item[price_columns[j]] = price_row[j]
    items.append(item)


items_to_json = {}
items_to_json['categories'] = categories
items_to_json['items'] = items


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.bool_):
            return bool(obj)
        return super(NpEncoder, self).default(obj)
    
with open('price.json', 'w') as json_file:
    json.dump(items_to_json, json_file, indent=1, ensure_ascii=False , cls=NpEncoder)





