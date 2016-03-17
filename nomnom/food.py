from slackbot.bot import respond_to
from slackbot.bot import listen_to
from scrape import ubereats, Cities
import re

@listen_to("what's for lunch today?", re.IGNORECASE)
def today(message):
    menus = ubereats(Cities.LOOP)
    msg = parseMenuToString(menus)

    message.send(msg)
    message.react('eggplant')

@listen_to("what's for lunch tomorrow?", re.IGNORECASE)
def tomorrow(message):
    menus = ubereats(Cities.LOOP, 1)
    msg = parseMenuToString(menus)

    message.send(msg)
    message.react('eggplant')

@listen_to('hello foodbot!')
def hi(message):
    message.reply('hello!')


def parseMenuToString(menus):
    msg = ''
    for menu in menus:
        msg += menu.fancyformat()
    if msg == '':
        msg = "Sorry, couldn't fetch the menus. Try again later"
    return msg