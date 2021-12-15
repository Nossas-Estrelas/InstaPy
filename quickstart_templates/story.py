# TO CORRECT SETUP INSTAPY SESSION READ THE DOCUMENTATIONS
from instapy import InstaPy
from instapy.util import smart_run
import schedule
import time
from datetime import datetime
import random
import requests

# generate random integer values
from random import choice
from random import seed
from random import randint
# seed random number generator
seed(1)

insta_username = 'nossasestrelas.br'
insta_password = '24072020'
session = InstaPy(username=insta_username, password=insta_password,
				  headless_browser=False, nogui=False, multi_logs=True)
followers_options = ['nossasestrelas.br', 'ricardonsantos1999']
followers_account = choice(followers_options)

with smart_run(session):
	#	ENVIA MENSAGEM PARA O TELEGRAM
	requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=html&text=Vendo story dos seguidores da conta: <b>{}</b>".format(followers_account))

	popeye_followers = session.grab_followers(username=followers_account, amount="full", live_match=True, store_locally=True)
	lazySmurf_following = session.grab_following(username=followers_account, amount="full", live_match=True, store_locally=True)
	session.story_by_users(popeye_followers+lazySmurf_following)																		#	VER STORY?

	requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-100159349166&parse_mode=html&text=Visualização de story dos seguidores da conta {} encerrada em {}"
				 .format(followers_account, datetime.now().strftime("%H:%M:%S")))