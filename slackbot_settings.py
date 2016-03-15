from apikeys import getSlackApiKey
API_TOKEN = getSlackApiKey()
default_reply = "Sorry but I didn't understand you"

PLUGINS = [
    'slackbot.plugins',
    'nomnom'
]
