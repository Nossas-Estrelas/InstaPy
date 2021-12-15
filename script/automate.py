import time
import datetime
from instapy.unfollow_util import unfollow
from instapy.plugins import InstaPyTelegramBot
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

insta_username = 'nossasestrelas.br'
insta_password = '24072020'
#	CONTAS
accounts_amout = random.randint(1, 5)
accounts_options = ['quadros__store',
					'geekstore',
					'quadrimundo',
					'quadrosgeek_loja',
					'quadrosing',
					'decoraflix',
					'artequadr0s',
					'we.placasdecorativas',
					'placasdecorativasslz',
					'placasem',
					'quadroscariri',
					'ideiapd',
					'artemdf.me',
					'placaspersonalizada',
					'placasdecorativaspro',
					'omg.placas',
					'placas_decorativas_em_mdf',
					'placasdecorativas.mdf',
					'placas.jm',
					'plaquinhasvintage',
					'placasart_',
					'jk_mdfpersonalizados',
					'd.decorpersonalizados',
					'al.placasdecorativas',
					'paulomdfsurubim',
					'vintageplacas',
					'decorarte.ofc',
					'sfx_placasdecorativas',
					'queroplac',
					'kg_placas_decorativas',
					'pignata_quadrinhos',
					'nataliaartesemmdf',
					'mw.mdf',
					'daminelliplacas',
					'decor_artes21',
					'enquadremdf',
					'jv.arte.decoracao',
					'pandaartof',
					'placdecor',
					'jotaerremdf',
					'abelabemcriativa',
					'oldwestboards',
					'alan_placas_descorativas',
					'decoradross',
					'performquadros_oficial',
					'retroplacasdecorativas',
					'nordeste_quadros',
					'quadrospersonalizadosam',
					'quadros_personalizados___',
					'_quadros__personalizados_',
					'quadrospersonalizados._',
					'quadrospersonalizadosmalta',
					'mariiames',
					'quadros_personalizados10',
					'quadrospersonalizados.7',
					'quadros.taveira',
					'_.quadrospersonalizados',
					'quadros_personalizadosss',
					'decor.goiania',
					#'lexshopee',
					'qua.drospersonalizados',
					'quadrospersonalizadosgyn',
					'atilaquadross',
					'ki_quadrospersonalizados',
					'arte_reis',
					'helena_theservices',
					'quadros_personalizados23',
					'quadrosseriesfilmes',
					'customicsheep',
					'dudabritoquadros',
					'loja.creativedecor',
					'arquecampos',
					'lojafabells',
					'quadrosemarte',
					'cantinho_quadros',
					'cativaarte',
					'j.t_personalizados',
					'quadrosspersonalizadoss',
					'overwallrecife',
					'vtquadros',
					'idcustomizados',
					'quadros.personaliza',
					'bi.quadros_',
					'art.vizzoni',
					'dekarts_store',
					'amorepresente1',
					'quadrospersonalizad0',
					'cah_personalizados_',
					'per.sonalizadosquadrosrj',
					'artepersonalizada_1',
					'lm_quadros_',
					'emoldurando.amor',
					'molduraafetiva',
					'quadros.personalizados.animes_',
					'quadros_personalizados_bh',
					'quadros.arts',
					'quadros_artkriativa',
					'belasartes.go',
					'emquadrosdesign',
					'decoracaocomquadros',
					'caprichosa_lettering',
					'retro_placasdecorativas',
					'couplepics07',
					'polaroid',
					'quadroscreareoficial',
					'polaroidagnus',
					'polaroids_davivi',
					'fran_polaroid',
					'polaroidstoree',
					'revels.polaroid',
					'dc.polaroids',
					'atelie.polaroids',
					'polaroidroads',
					'polaroidespace',
					'polaroidsarte',
					'minha.polaroidd',
					'polaroidscomproposito',
					'_jsquadros',
					#'polaroidphotos21',
					'polaroidedodia',
					'apolloquadros',
					'polariuspontocom',
					'polaroid.singular',
					'polaroidsretro',
					'juhquadrosdecorativos',
					'polaroidsdamay',
					'decore_recorde',
					'polaroid.eamor',
					'polaroidesdale',
					'polaroidapaulinha',
					'polaroidiando',
					'polaroidnageladeira',
					'polaroidsdagi',
					'polaroidcaico',
					'dona_polaroid_caruaru',
					'polaroidbycatelli',
					'placas.quadros.polaroides',
					'artes.gabs',
					'polaroidsdapaula',
					'polaroidtheparty',
					'polaroidee_',
					#'yas.polaroid',
					'polaroid_luarosa',
					'bemquadro',
					'polaroid2d',
					'allpolaroid',
					'beminefotos',
					'polaroidsdamary',
					'amorporpolaroids',
					'doce_polaroid',
					'amorpolaroids_',
					'polaroidsdakaren',
					'polaroidzou_',
					'picsnaths',
					'polaroidcolecionar',
					'polarone.id',
					'laripersonalizadosce']
random.shuffle(accounts_options)																												#	EMBARALHA A ORDEM DA LISTA
accounts_selected = accounts_options[:accounts_amout]																							#	SELECIONA UMA DAS CONTAS

#	HASHTAG
hashtag_amout = random.randint(10, 15)
hashtags_options = ['mdf', 'personalizado', 'quadro', 'placa', 'anime', 'fotos', 'diadosnamorados', 'casamento', 'natal', 'finaldeano', 'anonovo', 'mdf', 'mdfdecorado', 'pmdf', 'mdfpersonalizado', 'artesanatoemmdf', 'bpcaespmdf', '50anosdetrabalhocomcaespmdf', 'pmdfoficial', 'artesanatomdf', 'nomemdf', 'caixasmdf', 'mdfcru', 'caixamdf', 'maquiagemdf', 'arteemmdf', 'letramdf', 'quadrosmdf', 'pinturaemmdf', 'gtoppmdf', 'quadromdf', 'mdfnaparede', 'arvoremdf', 'caixademdf', 'amorecarinhonomdf', 'caixaemmdf', 'cbmdf', 'aulaopmdf', 'letrasmdf', 'artesanatoemdf', 'painelmdf']
random.shuffle(hashtags_options)
hashtags_selected = hashtags_options[:hashtag_amout]

#	LOCATION
location_options = ['c2781244/brasil-brazil', '112047398814697/sao-paulo-brazil', '103804601668795/belo-horizonte-minas-gerais', '213088733/brasilia-brazil', '213088533/rio-de-janeiro-rio-de-janeiro']

#	BUSINESS
target_business_categories = ['category1', 'category2', 'category3']
session = InstaPy(username=insta_username, password=insta_password, headless_browser=False, nogui=False, multi_logs=True)
telegram = InstaPyTelegramBot(token='1857488138:AAEc3WXaqvPv8woW-hTC7-iZCHAKjeJsO24', telegram_username='ricardonsantos1999', instapy_session=session)

def get_session():

	imessage = 'PREPARANDO LOGIN NA CONTA <strong>{}</strong>...'.format(insta_username)
	
	dont_likes = ['#exactmatch', '[startswith', ']endswith', 'broadmatch']
	ignore_users = ['studiolud.braga', 'user2', 'user3']

	ignore_list = ['porn', 'sex', 'dick', 'pussy']																									#	Ignorar postagens que contenham...

	#	DEFINE SUPERVISÂO PARA AS AÇÕES
	session.set_quota_supervisor(enabled=True, sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"], sleepyhead=True, stochastic_flow=True, notify_me=True, peak_likes_hourly=57, peak_likes_daily=585, peak_comments_hourly=21, peak_comments_daily=182, peak_follows_hourly=48, peak_follows_daily=None, peak_unfollows_hourly=35, peak_unfollows_daily=402, peak_server_calls_hourly=None, peak_server_calls_daily=4700)
	mset_quota_supervisor = '\n\n<strong>• set_quota_supervisor</strong>: ATIVADO'
	
	#	RELACIONAMENTO
	session.set_relationship_bounds(enabled=True, potency_ratio=None, delimit_by_numbers=True, max_followers=8500, max_following=3000, min_followers=25, min_following=25, min_posts=10)
	mset_relationship_bounds = '\n\n<strong>• set_relationship_bounds</strong>: ATIVADO\npotency_ratio=None\ndelimit_by_numbers=True\nmax_followers=8500\nmax_following=3000\nmin_followers=25\nmin_following=25\nmin_posts=10'

	#	DELAY (TEMPO DE ESPERA)
	session.set_action_delays(enabled=True, like=3.2, comment=5.1, follow=4.17, unfollow=28.1, story=15.3, randomize=True, random_range_from=70, random_range_to=140)
	mset_action_delays = '\n\n<strong>• set_action_delays</strong>: ATIVADO\nlike=3.2\ncomment=5.1\nfollow=4.17\nunfollow=28.1\nstory=15.3\nrandomize=True\nrandom_range_from=70\nrandom_range_to=140'

	#	FILTRO (IDIOMA - PULAR USUARIOS)
	session.set_mandatory_language(enabled=True, character_set=['LATIN'])
	mset_mandatory_language = '\n\n<strong>• set_mandatory_language</strong>: ATIVADO\nLATIN'
	session.set_skip_users(skip_private=True, private_percentage=100, skip_no_profile_pic=True, no_profile_pic_percentage=100, skip_business=True, skip_non_business=False, dont_skip_business_categories=[target_business_categories], business_percentage=100, skip_public=False, public_percentage=0)
	mset_skip_users = '\n\n<strong>• set_skip_users</strong>: ATIVADO\nprivate_percentage=100\nskip_no_profile_pic=True\nno_profile_pic_percentage=100\nskip_business=True\nskip_non_business=False\ndont_skip_business_categories=[{}]\nbusiness_percentage=100\nskip_public=False\npublic_percentage=0'.format(target_business_categories)


	friends = ['instagram']
	session.set_dont_include(friends)
	session.set_dont_like(dont_likes)
	session.set_ignore_if_contains(ignore_list)
	session.set_ignore_users(ignore_users)
	session.set_simulation(enabled=True)
	mset_dont_include = '\n\n<strong>• set_dont_include</strong>: ATIVADO\n{}'.format(('\n'.join(friends)))
	mset_dont_like = '\n\n<strong>• set_dont_like</strong>: ATIVADO\n{}'.format(('\n'.join(dont_likes)))
	mset_ignore_if_contains = '\n\n<strong>• set_ignore_if_contains</strong>: ATIVADO\n{}'.format(('\n'.join(ignore_list)))
	mset_ignore_users = '\n\n<strong>• set_ignore_users</strong>: ATIVADO\n{}'.format(('\n'.join(ignore_users)))
	mset_simulation = '\n\n<strong>• set_simulation</strong>: ATIVADO'

	session.set_user_interact(amount=random.randint(1, 2), randomize=True, percentage=random.randint(80, 100), media='Photo')
	session.set_do_like(enabled=True, percentage=random.randint(90, 100))
	session.set_do_comment(enabled=True, percentage=random.randint(50, 70))
	session.set_do_follow(enabled=True, percentage=random.randint(30, 50), times=1)
	session.set_do_story(enabled=True, percentage=random.randint(80, 100), simulate=False)

	session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
	session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
	session.set_blacklist(enabled=True, campaign="business_interact")

	mset_user_interact = '\n\n<strong>• set_user_interact</strong>: ATIVADO'
	mset_do_like = '\n\n<strong>• set_do_like</strong>: ATIVADO'
	mset_do_comment = '\n\n<strong>• set_do_comment</strong>: ATIVADO'
	mset_do_follow = '\n\n<strong>• set_do_follow</strong>: ATIVADO'
	mset_do_story = '\n\n<strong>• set_do_story</strong>: ATIVADO'
	#telegram.send_message(text="{}".format(imessage+mset_quota_supervisor+mset_relationship_bounds+mset_action_delays+mset_mandatory_language+mset_skip_users+mset_dont_include+mset_dont_like))
	#telegram.send_message(text="{}\n\n<b>• DATA E HORA •</b> {}".format(mset_ignore_if_contains+mset_ignore_users+mset_simulation+mset_user_interact+mset_do_like+mset_do_comment+mset_do_follow+mset_do_story,datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
	return session

#	FUNÇÕES
def viewstory():
	session = get_session()
	with smart_run(session):
		try:
			#	CONFIGURAÇÃO COMPLEMENTAR
			follower_account_select = choice(accounts_selected)
			follower_amount = random.randint(30, 60)
			popeye_followers = session.grab_followers(username=follower_account_select, amount=follower_amount, live_match=False, store_locally=True)
			#lazySmurf_following = session.grab_following(username=accounts_selected, amount="1", live_match=False, store_locally=True)

			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>INICIANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo da Ação:</b> Visualizando styories dos seguidores de: <b>{}</b> ({})\n\n"
			#"<b>• LISTA DE SEGUIDORES •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, follower_account_select, follower_amount, ('\n'.join(popeye_followers)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))

			#	ACTION
			session.story_by_users(popeye_followers)

			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>ENCERRANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo da Ação:</b> Visualizando styories dos seguidores de: <b>{}</b>\n\n"
			#"<b>• LISTA DE SEGUIDORES •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, follower_account_select, ('\n'.join(popeye_followers)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
		except Exception:
			print(traceback.format_exc())

def viewstory_followers():
	session = get_session()
	with smart_run(session):
		try:
			#	CONFIGURAÇÃO COMPLEMENTAR
			follower_account_select = choice(accounts_selected)
			follower_amount = 'full'
			popeye_followers = session.grab_followers(username=insta_username, amount=follower_amount, live_match=False, store_locally=True)
			#lazySmurf_following = session.grab_following(username=accounts_selected, amount="1", live_match=False, store_locally=True)

			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>INICIANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo da Ação:</b> Visualizando stories dos seguidores de: <b>{}</b> ({})\n\n"
			#"<b>• LISTA DE SEGUIDORES •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, insta_username, follower_amount, ('\n'.join(popeye_followers)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))

			#	ACTION
			session.story_by_users(popeye_followers)

			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>ENCERRANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo da Ação:</b> Visualizando stories dos seguidores de: <b>{}</b>\n\n"
			#"<b>• LISTA DE SEGUIDORES •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, insta_username, ('\n'.join(popeye_followers)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
		except Exception:
			print(traceback.format_exc())

def like_by_tags():
	session = get_session()
	with smart_run(session):
		try:
			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>INICIANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Curtindo publicações baseado em: <b>{} hashtags</b>\n\n"
			#"<b>• LISTA DE HASHTAGS •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, hashtag_amout, ('\n'.join(hashtags_selected)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))

			#	ACTION
			session.set_user_interact(amount=random.randint(3, 5), randomize=True, percentage=100)
			session.like_by_tags(hashtags_selected, amount=random.randint(5, 15), interact=True, use_smart_hashtags=False, use_smart_location_hashtags=False, randomize=True)

			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>ENCERRANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Curtindo publicações baseado em: <b>{} hashtags</b>\n\n"
			#"<b>• LISTA DE HASHTAGS •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, hashtag_amout, ('\n'.join(hashtags_selected)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
		except Exception:
			print(traceback.format_exc())

def unfollow_users():
	session = get_session()
	with smart_run(session):
		try:
			unfollow_time = 48*60*60
			lazySmurf_following1 = session.grab_following(username=insta_username, amount="full", live_match=False, store_locally=False)
			unfollow_amount = random.randint((int(len(lazySmurf_following1)/3)), int(len(lazySmurf_following1)))

			#telegram.send_message(text="<strong>INICIANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Deixando de seguir <b>{} usuarios</b> seguidos pelo script e que não são reciprocos durante <b>{} horas</b>\n\n"
			#"<b>• LISTA DE CONTAS SENDO SEGUIDAS ({}) •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, unfollow_amount, (int(unfollow_time/3600)), len(lazySmurf_following1), ('\n'.join(lazySmurf_following1)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))

			#	AÇÕES (DEIXAR DE SEGUIR USUARIOS SEGUIDOS PELO SCRIPT E QUE NÃO TE SEGUEM DE VOLTA POR 2 DIAS)
			session.unfollow_users(amount=unfollow_amount, instapy_followed_enabled=True, instapy_followed_param="all", style="RANDOM", unfollow_after=unfollow_time, sleep_delay=random.randint(50, 120))

			#popeye_followers = session.grab_followers(username=insta_username, amount='full', live_match=False, store_locally=False)
			lazySmurf_following2 = session.grab_following(username=insta_username, amount="full", live_match=False, store_locally=False)
			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>ENCERRANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Deixando de seguir <b>{} usuarios</b> seguidos pelo script e que não são reciprocos durante <b>{} horas</b>\n\n"
			#"<b>• LISTA DE CONTAS SENDO SEGUIDAS ({}) •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, unfollow_amount, (int(unfollow_time/3600)), len(lazySmurf_following2), ('\n'.join(lazySmurf_following2)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
		except Exception:
			print(traceback.format_exc())

def interact_target_accounts_and_influencers():
	session = get_session()
	with smart_run(session):
		try:
			#	DEFINIÇÕES LOCAIS
			comments = ['Acredita que apareceu no meu explorar? 🥰😍😘 @{}',
					'Eu amei @{}',
					'Que foto linda! @{}',
					'Eu amei o seu perfil! @{}',
					'Sempre fico feliz quando passa um post assim pelo meu feed :thumbsup:',
					'Simplesmente incrível :open_mouth:',
					'Amo seus posts @{}',
					'Olha que incrivel @{}',
					'Você é motivo de inspiração, sério @{}',
					'😎😎😎',
					'😁😁😁😁😁😁😁💪🏼',
					'😋🎉", "😀🍬',
					'🥰😍😘👈🏼👏🏼👏🏼',
					'🙂🚀🎊🎊🎊',
					'🥰😍😘',
					'❤',
					'🎉',
					'😎',
					'🥰😍😘🥰😍😘',
					'👏🏼😉',
					'Uma foto que define o quão incrível você é @{}',
					'A melhor foto que já apareceu no meu feed 🤩',
					'A melhor foto que apareceu hoje no meu feed 🤩',
					'Tem uma alegria em ti que vem lá de dentro',
					'Até por foto eu sinto a sua boa energia!',
					'Cada vez mais incrível 😉',
					'Você é pura luz! ✨',
					'Você é a alegria materializada!',
					'Parando o Instagram em 3, 2, 1...',
					'Ai, meu coração 😱😱',
					'Deus te fez de modo único!',
					'O teu entusiamos me contagia!',
					'O Facebook vai apresentar problemas o dia inteiro depois dessa foto bombástica 💥',
					'Blogueira poderosa!',
					'Encontre o defeito. Não existe.',
					'Fera 👏👏',
					'Arrasou demais, como sempre.',
					'Plenitude.',
					'Sou tua fã número ⬆️',
					'Que foto perfeita! Numa escala de 1 a 10, é 100.',
					'Iluminada de todas as maneiras!',
					'Afff, zero defeitos! 🥰🥰 @{}',
					'Acredita que apareceu no meu explorar?🥰😍😘\nEu amei @{}',
					'Que foto linda! @{}',
					'Eu amei o seu perfil! @{}',
					'Sempre fico feliz quando passa um post assim pelo meu feed :thumbsup:',
					'Simplesmente incrível :open_mouth:',
					'Amo seus posts @{}',
					'Olha que incrivel @{}',
					'Sempre me inspiro em você @{}',
					'Eu posso sentir sua paixão @{} :muscle:',
					'Que foto incrível! 😍 Você pode passar no meu perfil?',
					'Que foto incrível! 😍 Você já conhece a nossa loja aqui no Insta? 🥰😉😍',
					'Maravilhoso!! 😍 Seria ótimo se você desse uma olhada nas minhas fotos também! ',
					'Maravilhoso!! 😍 Eu ficaria honrado se você desse uma olhada em minhas imagens e me dissesse o que você acha 🥰😉😍',
					'Isso é incrível!! 😍 Algum comentário sobre minhas fotos? 🥰😉😍',
					'Isso é incrível!! 😍 talvez você goste das minhas fotos também? 🥰😉😍',
					'Eu realmente gosto da maneira como você capturou isso. Aposto que você também gosta das minhas fotos 🥰😉😍 ',
					'Eu realmente gosto da maneira como você capturou isso. Se tiver tempo, dê uma olhada nas minhas fotos também. Aposto que você vai gostar deles. 🥰😉😍',
					'Essa foto ta perfeita, sério!! 🥰😍😘',
					'Essa foto ficou ótima!! 🥰😍😘 :thumbsup: Será que você pode curtir o meu perfil?'
				]
			#session.set_comments(comments, media='Photo')

			#	Evite comentar e parar de seguir seus seguidores (as imagens ainda serão curtidas)
			friends = session.grab_followers(username=insta_username, amount='full', live_match=False, store_locally=True)
			session.set_dont_include(friends)

			#telegram.send_message(text="<strong>INICIANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Interação por <b>{}</b> hashtags (like)\n\n"
			#"<b>• LISTA DE HASHTAGS •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, hashtag_amout, ('\n'.join(hashtags_selected)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))

			#	Selecione usuários em uma lista de destinos predefinidos ...
			number = random.randint(5, 8)
			random_targets = accounts_options

			if len(accounts_options) <= number: random_targets = accounts_options
			else: random_targets = random.sample(accounts_options, number)

			#	Interaja com os alvos escolhidos...
			session.follow_user_followers(random_targets, amount=50, randomize=True, sleep_delay=600, interact=True)

			session.unfollow_users(amount=random.randint(75, 100), nonFollowers=True, style="FIFO", unfollow_after=24 * 60 * 60, sleep_delay=600)	#	Deixar de seguir não seguidores após 24 horas
			session.unfollow_users(amount=random.randint(75, 100), allFollowing=True, style="FIFO", unfollow_after=168 * 60 * 60, sleep_delay=600)	#	Deixar de seguir todos os usuários seguidos por InstaPy após 7 dias

			""" Joining Engagement Pods... """
			session.join_pods(topic='general', engagement_mode='heavy') 

			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>ENCERRANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Visualizando styories dos seguidores de: <b>{}</b>\n\n"
			#"<b>• LISTA DE SEGUIDORES •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, insta_username, ('\n'.join(insta_username)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
		except Exception:
			print(traceback.format_exc())

def interact_by_feed():
	session = get_session()
	with smart_run(session):
		try:
			#	DEFINIÇÕES LOCAIS
			comments = ['Acredita que apareceu no meu explorar?🥰😍😘\nEu amei @{}',
					'Que foto linda! @{}',
					'Eu amei o seu perfil! @{}',
					'Sempre fico feliz quando passa um post assim pelo meu feed :thumbsup:',
					'Simplesmente incrível :open_mouth:',
					'Amo seus posts @{}',
					'Olha que incrivel @{}',
					'Sempre me inspiro em você @{}',
					':raised_hands: Sim!',
					'Eu posso sentir sua paixão @{} :muscle:',
					'😎😎😎',
					'😁😁😁😁😁😁😁💪🏼',
					'😋🎉", "😀🍬',
					'😂😂😂👈🏼👏🏼👏🏼',
					'🙂🚀🎊🎊🎊',
					'😁😁😁',
					'😂',
					'🎉',
					'😎',
					'🤓🤓🤓🤓🤓',
					'👏🏼😉',
					'Que foto incrível! 😍 O que você acha da minha foto recente? ',
					'Que foto incrível! 😍 Eu acho que você também pode gostar do meu. 🥰😉😍',
					'Maravilhoso!! 😍 Seria ótimo se você desse uma olhada nas minhas fotos também! ',
					'Maravilhoso!! 😍 Eu ficaria honrado se você desse uma olhada em minhas imagens e me dissesse o que você pensa. 🥰😉😍',
					'Isso é incrível!! 😍 Algum comentário sobre minhas fotos? 🥰😉😍',
					'Isso é incrível!! 😍 talvez você goste das minhas fotos também? 🥰😉😍',
					'Eu realmente gosto da maneira como você capturou isso. Aposto que você também gosta das minhas fotos🥰😉😍 ',
					'Eu realmente gosto da maneira como você capturou isso. Se tiver tempo, dê uma olhada nas minhas fotos também. Aposto que você vai gostar deles. 🥰😉😍',
					'Ótima captura!! : smiley: Algum comentário sobre minha foto recente? 🥰😉😍',
					'Ótima captura!! : smiley:: thumbsup: O que você acha da minha foto recente? '
					]
						
			session.set_comments(comments, media='Photo')

			#telegram.send_message(text="<strong>INICIANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Interação por <b>{}</b> hashtags (like)\n\n"
			#"<b>• LISTA DE HASHTAGS •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, hashtag_amout, ('\n'.join(hashtags_selected)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))

			session.like_by_feed(amount=random.randint(75, 100), randomize=True, unfollow=False, interact=True)

			""" Joining Engagement Pods... """
			session.join_pods(topic='general', engagement_mode='heavy') 

			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>ENCERRANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Visualizando styories dos seguidores de: <b>{}</b>\n\n"
			#"<b>• LISTA DE SEGUIDORES •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, insta_username, ('\n'.join(insta_username)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
		except Exception:
			print(traceback.format_exc())


def model():
	session = get_session()
	with smart_run(session):
		try:
			#telegram.send_message(text="<strong>INICIANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Interação por <b>{}</b> hashtags (like)\n\n"
			#"<b>• LISTA DE HASHTAGS •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, hashtag_amout, ('\n'.join(hashtags_selected)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))

			session.like_by_tags(hashtags_selected, amount=random.randint(5, 15), interact=True, use_smart_hashtags=False, use_smart_location_hashtags=False, randomize=True)

			#	ENVIA MENSAGEM PARA O TELEGRAM
			#telegram.send_message(text="<strong>ENCERRANDO INTERAÇÃO</strong>\n\n\n"
			#"<b>• INFORMAÇÕES BÁSICAS •</b>\n<b>Usuário:</b> {}\n<b>Tipo:</b> Visualizando styories dos seguidores de: <b>{}</b>\n\n"
			#"<b>• LISTA DE SEGUIDORES •</b> \n{}"
			#"\n\n<b>• DATA E HORA •</b> {}".format(insta_username, insta_username, ('\n'.join(insta_username)), datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')))
		except Exception:
			print(traceback.format_exc())

interact_target_accounts_and_influencers()
#	LISTA DE TAREFAS
#	MANHÃ 																				(PRIMEIRO TURNO)
schedule.every().day.at("06:00").do(interact_by_feed)									#	INTERAGE DIRETAMENTE COM O FEED DA CONTA PRINCIPAL (SEGUIDORES)
schedule.every().day.at("07:28").do(viewstory)											#	VER STORY DE SEGUIDORES DE DETERMINADO USUARIO
schedule.every().day.at("09:45").do(interact_target_accounts_and_influencers)			#	INTERAGE COM CONTAS RELACIONADAS E INFLUENCIADORES DO MESMO RAMO DA CONTA PRINCIPAL
schedule.every().day.at("11:18").do(viewstory_followers)								#	VER STORY DE SEGUIDORES DO USUARIO PAGANTE

#	TARDE 																				(SEGUNDO TURNO)
schedule.every().day.at("11:45").do(interact_by_feed)									#	INTERAGE DIRETAMENTE COM O FEED DA CONTA PRINCIPAL (SEGUIDORES)
schedule.every().day.at("13:00").do(like_by_tags)										#	CURTIR POSTAGENS DE DETERMINADAS HASHTAGs
schedule.every().day.at("14:28").do(viewstory)											#	VER STORY DE SEGUIDORES DE DETERMINADO USUARIO
schedule.every().day.at("16:45").do(interact_target_accounts_and_influencers)			#	INTERAGE COM CONTAS RELACIONADAS E INFLUENCIADORES DO MESMO RAMO DA CONTA PRINCIPAL
schedule.every().day.at("17:18").do(viewstory_followers)								#	VER STORY DE SEGUIDORES DO USUARIO PAGANTE

#	NOITE 																				(TERCEIRO TURNO)
schedule.every().day.at("18:30").do(interact_by_feed)									#	INTERAGE DIRETAMENTE COM O FEED DA CONTA PRINCIPAL (SEGUIDORES)
schedule.every().day.at("20:45").do(viewstory_followers)								#	VER STORY DE SEGUIDORES DO USUARIO PAGANTE
schedule.every().day.at("22:45").do(interact_target_accounts_and_influencers)			#	INTERAGE COM CONTAS RELACIONADAS E INFLUENCIADORES DO MESMO RAMO DA CONTA PRINCIPAL

#	MADRUGADA 																			(QUARTO TURNO)
schedule.every().day.at("01:00").do(interact_target_accounts_and_influencers)			#	INTERAGE COM CONTAS RELACIONADAS E INFLUENCIADORES DO MESMO RAMO DA CONTA PRINCIPAL
schedule.every().day.at("04:00").do(viewstory)											#	VER STORY DE SEGUIDORES DE DETERMINADO USUARIO
schedule.every().day.at("05:15").do(unfollow_users)										#	DEIXA DE SEGUIR DETERMINADO NÚMERO DE CONTAS SEGUIDAS PELO SCRIPT QUE NÃO FOI CORRESPONDIDO EM ATÉ 48 HORAS


all_jobs = schedule.get_jobs()
#print(all_jobs)
#print(schedule.get_jobs()[1].do)
#print(schedule.get_jobs()[2].do)
#print('\n'.join(map(str, myall_jobss)))
#print(*all_jobs, sep = "\n")

for height in schedule.get_jobs() :
    print(height.do)

while True:
	schedule.run_pending()
	time.sleep(1)

