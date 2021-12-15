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


# generate random integer values
import random
from random import choice
from random import seed
from random import randint
# seed random number generator
seed(1)

from instapy import InstaPy
from instapy import smart_run

message = 'Olá, iniciando interação com o InstaPy:\n\nPROGRAMAÇÃO:\n07:36: Interact\n10:42: Viewstory\n11:00: Unfollow\n\n12:54: Interact\n16:20: Viewstory\n\n02:25: Unfollow'
insta_username = 'nossasestrelas.br'
insta_password = '24072020'
telegram_api = '1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24'
telegram_channel = '-1001593491663'
followers_options = ['quadros__store', 'geekstore']

requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=html&text=<b>{}</b>".format(message))
def get_session():
	session = InstaPy(username=insta_username,
					  password=insta_password,
					  headless_browser=False,
					  nogui=False,
					  multi_logs=True)

	return session

def interact():
	followers_account = choice(followers_options)
	# Send notification to my Telegram
	requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=MarkdownV2&text=Iniciando interação com seguidores de: *{}*".format(followers_account))

	# get a session!
	session = get_session()

	# let's go!
	with smart_run(session):
		counter = 0

		while counter < 5:
			counter += 1

			try:
				session.set_quota_supervisor(enabled=True,
                            sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                            sleepyhead=True,
                            stochastic_flow=True,
                            notify_me=True,
                            peak_likes_hourly=57,
                            peak_likes_daily=585,
                            peak_comments_hourly=21,
                            peak_comments_daily=182,
                            peak_follows_hourly=48,
                            peak_follows_daily=None,
                            peak_unfollows_hourly=35,
                            peak_unfollows_daily=402,
                            peak_server_calls_hourly=None,
                            peak_server_calls_daily=4700)

				hashtags = ['mdf', 'personalizado', 'quadro', 'placa', 'anime', 'fotos', 'diadosnamorados', 'casamento', 'natal', 'finaldeano', 'anonovo', 'mdf', 'mdfdecorado', 'pmdf', 'mdfpersonalizado', 'artesanatoemmdf', 'bpcaespmdf', '50anosdetrabalhocomcaespmdf', 'pmdfoficial', 'artesanatomdf', 'nomemdf', 'caixasmdf', 'mdfcru', 'caixamdf', 'maquiagemdf', 'arteemmdf', 'letramdf', 'quadrosmdf', 'pinturaemmdf', 'gtoppmdf', 'quadromdf', 'mdfnaparede', 'arvoremdf', 'caixademdf', 'amorecarinhonomdf', 'caixaemmdf', 'cbmdf', 'aulaopmdf', 'letrasmdf', 'artesanatoemdf', 'painelmdf']
				random.shuffle(hashtags)
				my_hashtags = hashtags[:10]
				
				#	RELACIONAMENTO
				session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=8500, max_following=4490, min_followers=100, min_following=56, min_posts=10, max_posts=1000)
				
				#	DELAY (TEMPO DE ESPERA)
				session.set_action_delays(enabled=True, like=3.2, comment=5.1, follow=4.17, unfollow=28.1, story=15.3, randomize=True, random_range_from=70, random_range_to=140)

				#	FILTRO (IDIOMA - LOCALIZAÇÃO - PULAR USUARIOS)
				session.set_mandatory_language(enabled=True, character_set=['LATIN'])
				session.set_smart_hashtags(my_hashtags, limit=10, sort='top', log_tags=True)
				session.set_smart_location_hashtags(['c2781244/brasil-brazil', '112047398814697/sao-paulo-brazil', '103804601668795/belo-horizonte-minas-gerais', '213088733/brasilia-brazil', '213088533/rio-de-janeiro-rio-de-janeiro'], radius=650, limit=10)
				session.set_skip_users(skip_private=True,
									private_percentage=100,
									skip_no_profile_pic=True,
									no_profile_pic_percentage=100,
									skip_business=True,
									skip_non_business=False,
									business_percentage=100,
									#skip_business_categories=['Advertising Agency', 'Advertising/Marketing', 'Art', 'Art Gallery', 'Art Museum', 'Artist', 'Arts & Entertainment', 'Arts & Humanities Website', 'Athlete', 'Auto Dealers', 'Business & Utility Services', 'Clothing Store', 'Community', 'Community Organization', 'Company', 'Consulting Agency', 'Content & Apps', 'Creators & Celebrities', 'Education', 'Food & Personal Goods', 'General Interest', 'Graphic Designer', 'Home Goods Stores', 'Home Services', 'Jewelry/Watches', 'Lifestyle Services', 'Local Business', 'Local Events', 'Management Service', 'Media/News Company', 'Non-Profits & Religious Organizations', 'Party Entertainment Service', 'Personal Goods & General Merchandise Stores', 'Product/Service', 'Professional Service', 'Professional Sports Team', 'Public Figure', 'Public Relations Agency', 'Publishers', 'Restaurants', 'Ski Resort', 'Sport', 'Sports & Recreation', 'Transportation & Accomodation Services', 'Travel Agency', 'Wine/Spirits'],
									#dont_skip_business_categories=['Photographer', 'Photography Videography'],
									skip_bio_keyword=[],
									mandatory_bio_keywords=[],
									skip_public=False,
									public_percentage=0)

				#	INTERAGIR?
				session.set_user_interact(amount=randint(1, 5), randomize=True, percentage=randint(50, 80))
				session.interact_user_followers([followers_account], amount=randint(15, 29), randomize=True)
				session.set_do_follow(enabled=True, percentage=random.randrange(30, 70))						#	SEGUIR?
				session.set_do_like(enabled=True, percentage=random.randrange(80, 100))							#	CURTIR?
				session.set_do_comment(enabled=True, percentage=randint(50, 80))								#	COMENTAR?
				session.set_do_story(enabled=True, percentage=randint(50, 80), simulate=False)					#	VER STORY?

				#	COMENTARIOS
				#session.set_mandatory_words(['#love', '#amor', '#esposa', '#namorada'])
				session.set_comments(["🔝🔝🔝", "👍", "🥰", "❤❤", "😍😍😍"])

			except Exception:
				print(traceback.format_exc())

	# Send notification to my Telegram
	requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=MarkdownV2&text=\nInteração com seguidores de {} encerrada".format(followers_account))

def interactLocation():
	#	DEFINE LOCALIZAÇÕES
	location_options = ['c2781244/brasil-brazil', '112047398814697/sao-paulo-brazil', '103804601668795/belo-horizonte-minas-gerais', '213088733/brasilia-brazil', '213088533/rio-de-janeiro-rio-de-janeiro']
	location_amount = randint(15, 40)

	#	BUSCA INFORMAÇÃO SOBRE O LOGIN
	session = get_session()
	with smart_run(session):
		counter = 0
		while counter < 5:
			counter += 1
			try:
				#	ENVIA MENSAGEM PARA O TELEGRAM
				requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=MarkdownV2&text=\n"
				"\tIniciando interação com postagens: *POR LOCALIZAÇÃO* (*{} postagens*)".format(location_amount))

				#	DEFINE SUPERVISÂO PARA AS AÇÕES
				session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True, peak_likes_hourly=57, peak_likes_daily=585, peak_comments_hourly=21, peak_comments_daily=182, peak_follows_hourly=48, peak_follows_daily=None, peak_unfollows_hourly=35, peak_unfollows_daily=402, peak_server_calls_hourly=None, peak_server_calls_daily=4700)

				#	RELACIONAMENTO
				session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=8500, max_following=4490, min_followers=100, min_following=56, min_posts=10, max_posts=1000)
				
				#	DELAY (TEMPO DE ESPERA)
				session.set_action_delays(enabled=True, like=3.2, comment=5.1, follow=4.17, unfollow=28.1, story=15.3, randomize=True, random_range_from=70, random_range_to=140)

				#	FILTRO (IDIOMA - PULAR USUARIOS)
				session.set_mandatory_language(enabled=True, character_set=['LATIN'])
				session.set_skip_users(skip_private=True, private_percentage=100, skip_no_profile_pic=True, no_profile_pic_percentage=100, skip_business=True, skip_non_business=False, business_percentage=100, skip_public=False, public_percentage=0)

				session.like_by_locations(location_options, amount=location_amount, skip_top_posts=False, randomize=True)										#	LIKE
				session.comment_by_locations(location_options, amount=location_amount, skip_top_posts=False)													#	COMMENTS
				session.set_comments(["🔝🔝🔝", "👍", "🥰", "❤❤", "😍😍😍"])																			   #   COMMENTS DEFINE
				#session.follow_by_locations(location_options, amount=location_amount, skip_top_posts=False)													#	FOLLOW	(SKIPPED)

			except Exception:
				print(traceback.format_exc())

	# Send notification to my Telegram
	requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=MarkdownV2&text=\n"
	"\tEncerrando interação com postagens: *POR LOCALIZAÇÃO*".format())

def InteractbyComments():
	#	DEFINE LOCALIZAÇÕES
	location_options = ['c2781244/brasil-brazil', '112047398814697/sao-paulo-brazil', '103804601668795/belo-horizonte-minas-gerais', '213088733/brasilia-brazil', '213088533/rio-de-janeiro-rio-de-janeiro']
	post_amount = randint(5, 10)
	random.shuffle(followers_options)
	my_followers_options = followers_options[:1]

	#	BUSCA INFORMAÇÃO SOBRE O LOGIN
	session = get_session()
	with smart_run(session):
		counter = 0
		while counter < 5:
			counter += 1
			try:
				#	ENVIA MENSAGEM PARA O TELEGRAM
				requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=MarkdownV2&text=\n"
				"\tIniciando interação em comentarios de postagens: *POR LOCALIZAÇÃO* (*{} postagens*)".format(post_amount))

				#	DEFINE SUPERVISÂO PARA AS AÇÕES
				session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True, peak_likes_hourly=57, peak_likes_daily=585, peak_comments_hourly=21, peak_comments_daily=182, peak_follows_hourly=48, peak_follows_daily=None, peak_unfollows_hourly=35, peak_unfollows_daily=402, peak_server_calls_hourly=None, peak_server_calls_daily=4700)

				#	RELACIONAMENTO
				session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=8500, max_following=4490, min_followers=100, min_following=56, min_posts=10, max_posts=1000)
				
				#	DELAY (TEMPO DE ESPERA)
				session.set_action_delays(enabled=True, like=3.2, comment=5.1, follow=4.17, unfollow=28.1, story=15.3, randomize=True, random_range_from=70, random_range_to=140)

				#	FILTRO (IDIOMA - PULAR USUARIOS)
				session.set_mandatory_language(enabled=True, character_set=['LATIN'])
				session.set_skip_users(skip_private=True, private_percentage=100, skip_no_profile_pic=True, no_profile_pic_percentage=100, skip_business=True, skip_non_business=False, business_percentage=100, skip_public=False, public_percentage=0)


				session.set_do_comment(enabled=True, percentage=14)
				session.set_comment_replies(replies=["{} 🔝🔝🔝", "{} 👍", "{} 🥰", "{} ❤❤", "{} 😍😍😍", "{} 😎😎😎", "{} 😁😁😁😁😁😁😁💪🏼", "{} 😋🎉", "{} 😀🍬", "{} 😂😂😂👈🏼👏🏼👏🏼", "{} 🙂🙋🏼‍♂️🚀🎊🎊🎊", "{} 😁😁😁", "{} 😂",  "{} 🎉",  "{} 😎", "{} 👏🏼😉"], media="Photo")

				session.set_user_interact(amount=2, percentage=70, randomize=True, media="Photo")
				session.set_do_like(enabled=True, percentage=100)

				session.interact_by_comments(usernames=my_followers_options, posts_amount=post_amount, comments_per_post=post_amount, reply=True, interact=True, randomize=True, media="Photo")
			except Exception:
				print(traceback.format_exc())

	# Send notification to my Telegram
	requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=MarkdownV2&text=\n"
	"\tEncerrando interação com postagens: *POR LOCALIZAÇÃO*".format())

def unfollow():
	unfollower = random.randrange(10, 50)
	requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=MarkdownV2&text=Deixando de serguir no máximo: *{} contas*".format(unfollower))
	

	# get a session!
	session = get_session()

	# let's go!
	with smart_run(session):
		try:
			# settings
			session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

			# actions
			session.unfollow_users(amount=unfollower, allFollowing=False, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=3)

		except Exception:
			print(traceback.format_exc())

	requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=MarkdownV2&text=InstaPy Unfollower Stoped")

def viewstory():
	session = get_session()

	
	session.set_quota_supervisor(enabled=True,
                            sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                            sleepyhead=True,
                            stochastic_flow=True,
                            notify_me=True,
                            peak_likes_hourly=57,
                            peak_likes_daily=585,
                            peak_comments_hourly=21,
                            peak_comments_daily=182,
                            peak_follows_hourly=48,
                            peak_follows_daily=None,
                            peak_unfollows_hourly=35,
                            peak_unfollows_daily=402,
                            peak_server_calls_hourly=None,
                            peak_server_calls_daily=4700)
	with smart_run(session):
		try:
			followers_account = choice(followers_options)
			#	ENVIA MENSAGEM PARA O TELEGRAM
			requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=html&text=Vendo story dos seguidores da conta: <b>{}</b>".format(followers_account))

			popeye_followers = session.grab_followers(username=followers_account, amount=randint(30, 60), live_match=False, store_locally=True)
			#lazySmurf_following = session.grab_following(username=followers_account, amount="1", live_match=False, store_locally=True)
			session.story_by_users(popeye_followers)

			requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-100159349166&parse_mode=html&text=Visualização de story dos seguidores da conta {} encerrada em {}".format(followers_account, datetime.now().strftime("%H:%M:%S")))
			session.set_do_story(enabled=True, percentage=randint(99, 100), simulate=False)					#	VER STORY?
		except Exception:
			print(traceback.format_exc())


# schedulers
schedule.every().day.at("07:36").do(interact)
schedule.every().day.at("10:42").do(viewstory)
schedule.every().day.at("11:00").do(unfollow)

schedule.every().day.at("11:55").do(interact)
schedule.every().day.at("14:10").do(interactLocation)
schedule.every().day.at("14:00").do(InteractbyComments)
schedule.every().day.at("14:37").do(viewstory)

schedule.every().day.at("18:00").do(interact)
schedule.every().day.at("03:39").do(viewstory)

#schedule.every().day.at("02:25").do(unfollow)

#schedule.every().wednesday.at("03:00").do(xunfollow)

while True:
	schedule.run_pending()
	time.sleep(1)
