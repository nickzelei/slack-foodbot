import json
import requests
from datetime import date, timedelta

class Menu:
    def __init__(self, r, des, dish, price):
        self.restaurant = r
        self.description = des
        self.dish = dish
        self.price = price

    def fancyformat(self):
        return self.restaurant + "\n" +\
               self.dish + " - " + self.price + "\n" +\
               self.description +\
               "\n----------\n"

def ubereats():
    data = {'city': 'CHI'}
    headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8'}
    response = requests.post('https://ubereats-city.appspot.com/_api/menus.get', headers=headers, data=json.dumps(data))
    jsonData = response.json()

    # timestamp = str(date.today() + timedelta(days=1)) + "T00:00:00"
    timestamp = str(date.today()) + "T00:00:00"

    menus = []
    menuData = jsonData.get("menu", {})
    for day in menuData:
        if day.get("date") == timestamp:
            meals = day.get("meals", {})
            for meal in meals:
                m = Menu(meal.get("restaurant", ''), meal.get("description", ''), meal.get("dish", ''), meal.get("price", ''))
                menus.append(m)
            break
    return menus