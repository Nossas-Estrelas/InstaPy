import time
from datetime import datetime
import schedule
import traceback
import requests


# generate random integer values
import random
# seed random number generator
random.seed(1)

from instapy import InstaPy
from instapy import smart_run

message = 'Olá, iniciando interação com o InstaPy:\n\nPROGRAMAÇÃO:\n07:36: Interact\n10:42: Viewstory\n11:00: Unfollow\n\n12:54: Interact\n16:20: Viewstory\n\n02:25: Unfollow'
insta_username = 'nossasestrelas.br'
insta_password = '24072020'

date = datetime.now().strftime("%H:%M:%S")
#	CONTAS
accounts_amout = random.randint(1, 5)
accounts_options = ['quadros__store', 'geekstore', 'quadrimundo', 'quadrosgeek_loja', 'quadrosing', 'decoraflix']								#	DEFINE AS CONTAS INTERESSANTES
random.shuffle(accounts_options)																												#	EMBARALHA A ORDEM DA LISTA
accounts_selected = accounts_options[:accounts_amout]																							#	SELECIONA UMA DAS CONTAS

#	HASHTAG
hashtag_amout = random.randint(10, 15)
hashtags_options = ['mdf', 'personalizado', 'quadro', 'placa', 'anime', 'fotos', 'diadosnamorados', 'casamento', 'natal', 'finaldeano', 'anonovo', 'mdf', 'mdfdecorado', 'pmdf', 'mdfpersonalizado', 'artesanatoemmdf', 'bpcaespmdf', '50anosdetrabalhocomcaespmdf', 'pmdfoficial', 'artesanatomdf', 'nomemdf', 'caixasmdf', 'mdfcru', 'caixamdf', 'maquiagemdf', 'arteemmdf', 'letramdf', 'quadrosmdf', 'pinturaemmdf', 'gtoppmdf', 'quadromdf', 'mdfnaparede', 'arvoremdf', 'caixademdf', 'amorecarinhonomdf', 'caixaemmdf', 'cbmdf', 'aulaopmdf', 'letrasmdf', 'artesanatoemdf', 'painelmdf']
random.shuffle(hashtags_options)
hashtags_selected = hashtags_options[:hashtag_amout]

#	LOCATION
location_options = ['c2781244/brasil-brazil', '112047398814697/sao-paulo-brazil', '103804601668795/belo-horizonte-minas-gerais', '213088733/brasilia-brazil', '213088533/rio-de-janeiro-rio-de-janeiro']

session = InstaPy(username=insta_username, password=insta_password, headless_browser=False, nogui=False, multi_logs=True)
session.login()

#	ENVIA MENSAGEM PARA O TELEGRAM
requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=html&text=<strong>INICIANDO INTERAÇÃO</strong>\n\n\n"
"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo da Ação:</b> Interação por <b>{}</b> hashtags (like)\n\n"
"<b>• LISTA DE HASHTAGS •</b> \n{}"
"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, hashtag_amout, ('\n'.join(hashtags_selected)), datetime.now().strftime("%H:%M")))

#	DEFINE SUPERVISÂO PARA AS AÇÕES
session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True, peak_likes_hourly=57, peak_likes_daily=585, peak_comments_hourly=21, peak_comments_daily=182, peak_follows_hourly=48, peak_follows_daily=None, peak_unfollows_hourly=35, peak_unfollows_daily=402, peak_server_calls_hourly=None, peak_server_calls_daily=4700)
session.set_do_story(enabled=True, percentage=random.randint(80, 100), simulate=False)

#	RELACIONAMENTO
session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=8500, max_following=4490, min_followers=100, min_following=56, min_posts=10, max_posts=1000)
				
#	DELAY (TEMPO DE ESPERA)
session.set_action_delays(enabled=True, like=3.2, comment=5.1, follow=4.17, unfollow=28.1, story=15.3, randomize=True, random_range_from=70, random_range_to=140)

#	FILTRO (IDIOMA - PULAR USUARIOS)
session.set_mandatory_language(enabled=True, character_set=['LATIN'])
session.set_skip_users(skip_private=True, private_percentage=100, skip_no_profile_pic=True, no_profile_pic_percentage=100, skip_business=True, skip_non_business=False, business_percentage=100, skip_public=False, public_percentage=0)

#	AÇÕES (CURTIR E INTERAGIR POR TAGs)
session.set_user_interact(amount=random.randint(3, 5), randomize=True, percentage=100, media='None')
session.like_by_tags(hashtags_selected, amount=random.randint(5, 15), interact=True, use_smart_hashtags=False, use_smart_location_hashtags=False, randomize=True)

#	AÇÕES (CURTIR, INTERAGIR e COMENTAR POR LOCALIZAÇÃO)
session.set_user_interact(amount=random.randint(3, 5), randomize=True, percentage=100, media='None')
session.like_by_locations(location_options, amount=random.randint(15, 40), skip_top_posts=False, randomize=True)					 #   LIKE
session.comment_by_locations(location_options, amount=random.randint(15, 40), skip_top_posts=False)									 #	 COMMENTS
session.set_comments(["🔝🔝🔝", "👍", "🥰", "❤❤", "😍😍😍"])																	#   COMMENTS DEFINE

#	AÇÕES (CURTIR e COMENTAR BASEADO NOS COMENTARIOS DA POSTAGEM)
session.set_do_comment(enabled=True, percentage=random.randint(90, 100))
session.set_comment_replies(replies=["{} 🔝🔝🔝", "{} 👍", "{} 🥰", "{} ❤❤", "{} 😍😍😍", "{} 😎😎😎", "{} 😁😁😁😁😁😁😁💪🏼", "{} 😋🎉", "{} 😀🍬", "{} 😂😂😂👈🏼👏🏼👏🏼", "{} 🙂🙋🏼‍♂️🚀🎊🎊🎊", "{} 😁😁😁", "{} 😂",  "{} 🎉",  "{} 😎", "{} 👏🏼😉"])
session.set_user_interact(amount=random.randint(2, 5), percentage=random.randint(90, 100), randomize=True)
session.set_do_like(enabled=True, percentage=random.randint(70, 100))
session.interact_by_comments(usernames=accounts_selected, posts_amount=random.randint(5, 10), comments_per_post=random.randint(5, 10), reply=True, interact=True, randomize=True)

#	AÇÕES (VER STORY DE SEGUIDORES DE UMA CONTA)
popeye_followers = session.grab_followers(username=accounts_selected, amount=random.randint(30, 60), live_match=False, store_locally=True)
#lazySmurf_following = session.grab_following(username=accounts_selected, amount="1", live_match=False, store_locally=True)
session.story_by_users(popeye_followers)

#	AÇÕES (DEIXAR DE SEGUIR USUARIOS SEGUIDOS PELO SCRIPT E QUE NÃO TE SEGUEM DE VOLTA POR 2 DIAS)
session.unfollow_users(amount=random.randint(50, 120), instapy_followed_enabled=True, instapy_followed_param="all", style="RANDOM", unfollow_after=48*60*60, sleep_delay=random.randint(50, 120))

#	ENVIA MENSAGEM PARA O TELEGRAM
requests.get("https://api.telegram.org/bot1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24/sendMessage?chat_id=-1001593491663&parse_mode=html&text=<strong>ENCERRANDO INTERAÇÃO</strong>\n\n\n"
"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo da Ação:</b> Interação por <b>{}</b> hashtags (like)\n\n"
"<b>• LISTA DE HASHTAGS •</b> \n{}"
"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, hashtag_amout, ('\n'.join(hashtags_selected)), datetime.now().strftime("%H:%M")))