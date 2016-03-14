from slackbot.bot import respond_to
from slackbot.bot import listen_to
from scrape import ubereats
import re

@listen_to("what's for lunch today?", re.IGNORECASE)
def hey(message):
    menus = ubereats()
    msg = ''
    for menu in menus: msg += menu.fancyformat()
    if msg == '':
        msg = "Sorry, couldn't fetch the menus. Try again later"
    message.send(msg)
    message.react('eggplant')

@listen_to('hello foodbot!')
def hi(message):
    message.reply('hello!')