import twitter
import random
import giphypop
import configparser
import os


def publish():
    config = configparser.ConfigParser()

    for loc in os.curdir, os.path.expanduser("~"), "/etc/bot", os.environ.get("BOT_CONF"):
        if os.path.isfile(loc + "/bot.conf"):
            print(loc + "/bot.conf")
            config.read(loc + "/bot.conf")
            break

    twitterConsumerKey = config["twitter"]["consumerKey"]
    twitterConsumerSecret = config["twitter"]["consumerSecret"]
    twitterAccessTokenKey = config["twitter"]["AccessTokenKey"]
    twitterAccessTokenSecret = config["twitter"]["AccessTokenSecret"]
    giphyToken = config["giphy"]["token"]

    twitterApi = twitter.Api(consumer_key=twitterConsumerKey,
                             consumer_secret=twitterConsumerSecret,
                             access_token_key=twitterAccessTokenKey,
                             access_token_secret=twitterAccessTokenSecret)

    twitterApi.VerifyCredentials()

    trendsList = twitterApi.GetTrendsCurrent()
    selectedTrend = random.choice(trendsList)

    giphyApi = giphypop.Giphy(giphyToken)

    giphyResultList = [x for x in giphyApi.search(selectedTrend.name)]

    if len(giphyResultList) > 0:
        selectedGif = random.choice(giphyResultList)
    else:
        selectedGif = giphyApi.screensaver()

    twitterApi.PostUpdate(selectedTrend.name + " " + selectedGif.url)
