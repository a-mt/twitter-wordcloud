# Twitter Wordcloud

Generate a wordcloud of your tweeter feed

![](https://i.imgur.com/2q2PEi1t.png) ![](https://i.imgur.com/bAoEtTht.png) ![](https://i.imgur.com/BWKsfFXt.png)

## Install dependencies

    sudo apt-get install python-dev
    sudo pip install python-dotenv tweepy wordcloud stop-words numpy

## Create a Twitter app

* Go to https://app.twitter.com
* Create your app
* Retrieve your consumer key and consumer secret
* Create an access token for your own account
* Create a file `.env` with your credentials

      CONSUMER_KEY="xxxx"
      CONSUMER_SECRET="xxxx"
      ACCESS_TOKEN="xxxx"
      ACCESS_SECRET="xxxx"

## Run

    python app.py

Creates `output.png`, `output_grey.png`, `output_color.png`