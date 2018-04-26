import tweepy, random
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from stop_words import get_stop_words
from numpy import asarray
from dotenv import load_dotenv
import urllib3, Image, re, os

urllib3.disable_warnings()
load_dotenv(dotenv_path='./.env')

# Login to Tweeter
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_SECRET"))
 
api = tweepy.API(auth)

# Retrieve tweets
tweets_path = "./tweets"
if not os.path.isfile(tweets_path) or os.path.getsize(tweets_path) == 0:
    f = open(tweets_path, 'w')

    for status in api.user_timeline():
        f.write(api.get_status(status.id).text.encode("utf8"))
    f.close()

# Retrieve words from tweets
words=' '
count=0

f = open(tweets_path, 'r')
for line in f:
    words=words + re.sub('https://t.co/[^ ]+ ', '', line)
f.close

# Retrieve stopwords
stop_words = get_stop_words('en')

# Build wordcloud
logomask = asarray(Image.open('twitter_mask.png'))

wordcloud = WordCloud(
    stopwords=STOPWORDS.union(stop_words),
    background_color='black',
    max_words=500,
    mask=logomask,
    width=900,
    height=700
).generate(words)

#-------------------------------------------------------------------------------
# Normal
wordcloud.to_file("output.png")

#-------------------------------------------------------------------------------
# Turn to grey shades
def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    """
    Outputs a random hue saturation color value for a random shade of gray
    """
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

wordcloud.recolor(color_func=grey_color_func, random_state=3)
wordcloud.to_file("output_grey.png")

#-------------------------------------------------------------------------------
# Colorize with an image's colors
img_coloring = asarray(Image.open("twitter_colors.png"))
image_colors = ImageColorGenerator(img_coloring)

wordcloud.recolor(color_func = image_colors)
wordcloud.to_file("output_color.png")