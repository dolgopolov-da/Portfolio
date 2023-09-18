import pandas as pd
import gspread
from df2gspread import df2gspread as d2g
from oauth2client.service_account import ServiceAccountCredentials
import json
import datetime
import glob
import os
from dotenv import load_dotenv

load_dotenv()

'1. Подготовка'
json_key = os.getenv('JSON_KEY')
with open(json_key, 'r') as j:
    contents = json.loads(j.read())
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
my_mail = os.getenv('MY_MAIL')

'2. Авторизация'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key, scope)
gs = gspread.authorize(credentials)

'3. Название и создание листа в google sheets, делаем его видимым'
table_name = 'LandPlots'
sheet = gs.create(table_name)
sheet.share(my_mail, perm_type='user', role='writer')

'4. Загрузка датафрейма в google sheets'
month = datetime.datetime.today().strftime('%Y.%m')
day = datetime.datetime.today().strftime('%Y.%m.%d')

# заменить при необходимости
folder_path = f'landplots/adds_by_{month}/{day}'

files = glob.glob(f'{folder_path}/*.csv')
file_name = files[0]
df = pd.read_csv(file_name).drop(columns='Unnamed: 0')

sheet_name = 'Stavropol_region'
d2g.upload(df, table_name, sheet_name, credentials=credentials, row_names=True)
spreadsheet_url = "https://docs.google.com/spreadsheets/d/%s" % sheet.id
print(spreadsheet_url)

