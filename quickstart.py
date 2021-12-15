import requests
from datetime import datetime

from instapy import InstaPy

session = InstaPy(username="nossasestrelas.br", password="24072020")
requests.get(
        "https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-621978657&text='InstaPy Follower Started @ {}'"
            .format(datetime.now().strftime("%H:%M:%S")))
session.login()

#session.unfollow_users(amount = 10, allFollowing = True, unfollow_after = 0, sleep_delay = 600)
session.unfollow_users(amount=7000, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=3)

session.end()
