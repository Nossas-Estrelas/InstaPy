"""
This template is written by @Mehran

What does this quickstart script aim to do?
- My quickstart is just for follow/unfollow users.

NOTES:
- It uses schedulers to trigger activities in chosen hours and also, sends me
  messages through Telegram API.
"""

# -*- coding: UTF-8 -*-
import time
from datetime import datetime
import schedule
import traceback
import requests

from instapy import InstaPy
from instapy import smart_run

insta_username = 'nossasestrelas.br'
insta_password = '24072020'


def get_session():
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False,
                      nogui=False,
                      multi_logs=True)

    return session


def follow():
    # Send notification to my Telegram
    requests.get(
        "https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-621978657&text='InstaPy Follower Started @ {}'"
            .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()
    session.set_action_delays(enabled=True, like=3, comment=5, follow=4.17, unfollow=28, story=10, randomize=True, random_range_from=70, random_range_to=140)
    
    # let's go!
    with smart_run(session):
        counter = 0
        while counter < 2:
            counter += 1
            try:
                session.set_user_interact(amount=3, randomize=True, percentage=70, media='Photo')
                session.set_relationship_bounds(enabled=True, potency_ratio=None, delimit_by_numbers=True, max_followers=3000, max_following=900, min_followers=50, min_following=50)
                session.set_simulation(enabled=False)
                session.set_do_like(enabled=True, percentage=70)
                session.set_ignore_users([])
                session.set_do_comment(enabled=True, percentage=35)
                session.set_do_follow(enabled=True, percentage=25, times=1)
                session.set_comments(["🥰", "👍"])
                session.set_ignore_if_contains([])
                session.set_action_delays(enabled=True, like=40)

                # activity
                session.interact_user_followers(['mdf', 'papelaria', 'personalizados', 'quadros', 'únicos', 'fotos', 'impressão'], amount=10)

                """ Joining Engagement Pods...
                """
                session.join_pods(topic='entertainment', engagement_mode='no_comments')

            except Exception:
                print(traceback.format_exc())

    # Send notification to my Telegram
    requests.get(
        "https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-621978657&text='InstaPy Follower Stopped @ {}'"
        .format(datetime.now().strftime("%H:%M:%S")))


def unfollow():
    requests.get(
        "https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-621978657&text"
        "='InstaPy Unfollower Started @ {}'"
        .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()
    session.set_action_delays(enabled=True, like=3, comment=5, follow=4.17, unfollow=28, story=10, randomize=True, random_range_from=70, random_range_to=140)

    # let's go!
    with smart_run(session):
        try:
            # settings
            session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

            # actions
            session.unfollow_users(amount=600, allFollowing=True,
                                   style="RANDOM", sleep_delay=450)

        except Exception:
            print(traceback.format_exc())

    requests.get(
        "https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-621978657&text"
        "='InstaPy Unfollower Stopped @ {}'"
        .format(datetime.now().strftime("%H:%M:%S")))

# schedulers
schedule.every().day.at("22:41").do(follow)
schedule.every().day.at("00:05").do(unfollow)

#schedule.every().wednesday.at("03:00").do(xunfollow)

while True:
    schedule.run_pending()
    time.sleep(1)
