import twitter
import random
import giphypop
import configparser


def publish():


    config = configparser.ConfigParser()
    config.read("../config/bot.conf")
    
    twitterConsumerKey = config.get("twitter").consumerKey
    #"PrKFfSPiWmBqCW1uF2SHVbdRc"
    twitterConsumerSecret = 'D2pwLXbvUAHuggbmiOunRKKC3zgEeupusLZ09pHphF6O4vpXJJ'
    twitterAccessTokenKey = '930711782603350018-ehkGvUlOr8E2tZafX2stzXeWIj7lQjv'
    twitterAccessTokenSecret = 'FnDAGhzXB2ST7jgZw1NQRlxwR4h1YhqtHiAHIiEp1O30S'

    giphyToken = "ozGxgw025Wm1VtQlPPsmGF7p4AOG3Vef"



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
