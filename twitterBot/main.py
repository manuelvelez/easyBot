import twitter
import random
import giphypop
import configparser


def publish():


    config = configparser.ConfigParser()
    config.read("../config/bot.conf")

    twitterConsumerKey = config.get("twitter").consumerKey
    twitterConsumerSecret = config.get("twitter").consumerSecret
    twitterAccessTokenKey = config.get("twitter").AccessTokenKey
    twitterAccessTokenSecret = config.get("twitter").AccessTokenSecret
    giphyToken = config.get("giphy").token



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

#Create a video with my pictures and ffmpg
