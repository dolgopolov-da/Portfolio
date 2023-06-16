#!/home/httpd/vhosts/rooreeroo.mcdir.ru/private/venvs/myvenv/bin/python3.6
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, make_response
import json
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


@app.route("/shop", methods=['GET', 'POST'])
def shop_form():
    if request.method == 'GET':
        return render_template("site_form.html")
    elif request.method == 'POST':
        data = request.get_data().decode('utf-8')
        data = json.loads(data)
        send_email(data)

        response = make_response("Status Code: 200 OK")
        response.headers["Access-Control-Allow-Origin"] = "http://rooreeroo.mcdir.ru"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "*"
        response.headers["Access-Control-Allow-Credentials"] = True
        return response


def send_email(message):
    sender = 'dima.greensfan@gmail.com'
    password = 'ftzzoeeyomgitpqe'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    true, false = True, False
    basket_list = []
    for i in range(len(message['items'])):
        item = f"{i+1}. {message['items'][i]['_id']} {message['items'][i]['title']}: {message['items'][i]['amount']} шт."
        basket_list.append(item)

    final_message = \
    f'''
    Данные заказчика:
    ФИО: {message["name"]}
    Телефон: {message["phone"]}
    E-mail: {message["email"]}
    Адрес доставки: {message["address"]}

    Состав заказа:
    '''
    for i in range(len(basket_list)):
        final_message += f'\n{basket_list[i]}'

    try:
        server.login(sender, password)
        msg = MIMEText(str(final_message))
        msg['Subject'] = 'НОВЫЙ ЗАКАЗ НА САЙТЕ!'
        server.sendmail(sender, sender, msg.as_string())
        return 'The message was sent successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password, please!'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
