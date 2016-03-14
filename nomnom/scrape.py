import json
import requests
from datetime import date, timedelta

class Menu:
    def __init__(self, r, des, dish, price):
        self.restaurant = r
        self.description = des
        self.dish = dish
        self.price = price


def ubereats():
    data = {'city': 'CHI'}
    headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8'}
    response = requests.post('https://ubereats-city.appspot.com/_api/menus.get', headers=headers, data=json.dumps(data))
    jsonData = response.json()

    timestamp = str(date.today() + timedelta(days=2)) + "T00:00:00"

    menus = []
    for day in jsonData["menu"]:
        if day["date"] == timestamp:
            for meal in day["meals"]:
                m = Menu(meal["restaurant"], meal["description"], meal["dish"], meal["price"])
                menus.append(m)
            break

    return menus