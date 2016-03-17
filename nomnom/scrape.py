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

class Cities:
    LOOP = "CHI"
    NORTHWEST = "CHI_NORTHWEST"

headers = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json;charset=UTF-8'}
url = 'https://ubereats-city.appspot.com/_api/menus.get'

def ubereats(city, dayOffset = 0):
    try:
        if dayOffset < 0:
            dayOffset = 0
    except TypeError:
        dayOffset = 0

    data = {'city': city}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    jsonData = response.json()

    timestamp = str(date.today() + timedelta(days=dayOffset)) + "T00:00:00"

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