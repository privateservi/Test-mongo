import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '24652824'))
API_HASH = environ.get('API_HASH', 'eaca6d81c81f01149442cfeee6dbb4be')
BOT_TOKEN = environ.get('BOT_TOKEN', "6825470552:AAGJS_myT3Xe2pAdLRX5Sbv5YHQIKvgVv2U")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/47d57543609f1faddbc6a.jpg https://graph.org/file/fee3dafdacf11af114a59.jpg https://graph.org/file/6038dbae3bd8e5cb44897.jpg https://graph.org/file/f735645d19aabd6d25d17.jpg https://graph.org/file/5ce463e5a2edf56470bb6.jpg https://graph.org/file/e101e043cab0269091c9d.jpg https://graph.org/file/fc2aebe2ebfe6808660ad.jpg https://graph.org/file/93254e40bd10e6fbeae5c.jpg https://graph.org/file/28c43ebc4de422f24b182.jpg https://graph.org/file/8f8cbdf63f0eeb235cc3f.jpg https://graph.org/file/9dbdb9f86952c106f9131.jpg https://graph.org/file/c6ac894696d5157c80964.jpg https://graph.org/file/ed2fb77f665081e916abb.jpg https://graph.org/file/0362105a1347d200a9667.jpg https://graph.org/file/57e5850ec173cc1db68da.jpg https://graph.org/file/473226bc919bd7524069c.jpg https://graph.org/file/1f129ddabdc480c6906af.jpg https://graph.org/file/8e87d194c787909c9c276.jpg https://graph.org/file/9c8504c9e43ad2f818f14.jpg https://graph.org/file/13f8f4d4b920b1ebe8792.jpg https://graph.org/file/a9a1413dee9df96872335.jpg https://graph.org/file/8e8c8912fb6aaf95fe1c2.jpg https://graph.org/file/3bc305e2288b24fd7913d.jpg https://graph.org/file/01ead07a6a742e67fa6bb.jpg https://graph.org/file/6a2dcd1f53f5b52de571c.jpg https://graph.org/file/49b217f0c63f3102a818c.jpg https://graph.org/file/f56a4041c05970f9835e7.jpg https://graph.org/file/3816445f78627859a257c.jpg https://graph.org/file/36eab7c50c2fea1db9c8e.jpg https://graph.org/file/2a73975d17aa75d4037c6.jpg https://graph.org/file/09d93ed056ff26f36fb56.jpg https://graph.org/file/e31b9dea19a627ddb0bfb.jpg https://graph.org/file/e84ad342a34172dbd6a14.jpg https://graph.org/file/1a2c4fa5e06670f7fd185.jpg https://graph.org/file/90872db0d0c6d23da0e29.jpg https://graph.org/file/85e18f57931e0f9498a5a.jpg https://graph.org/file/cb074803c16510e6d1c14.jpg https://graph.org/file/979cc7a3e3aaf5e9b412b.jpg https://graph.org/file/660718b9e623791974493.jpg https://graph.org/file/ef0e2897ddf5c8df82058.jpg https://graph.org/file/d3b93745600f2730a637d.jpg https://graph.org/file/9a3813b0755d25ea63800.jpg https://graph.org/file/55753abeb28db5c7a593b.jpg https://graph.org/file/e11d1f86a5589bae87f26.jpg https://graph.org/file/2bc7aa67b8e1e93265a04.jpg https://graph.org/file/bcbb9e4409c27134cce6c.jpg https://graph.org/file/f857e90b2452888611930.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/e0770294280f17df23911.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/5f4126f0a68828857243f.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/f6466cc7f17f54ab0ff3e.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '885675538').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002072864187').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '885675538').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1001457939263')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://smdfiletertest:smdfiletertest10@cluster0.bfkvuuf.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'upshrink.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '0b43fe204c82d7e5f0fb6bd02ca125f4260f871b')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+oZ27l2vnexphZTVl')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/SAM_DUB_LEZHa')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/SMD_Dulinks')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', '⚓𝐒𝐌𝐃_BOTz🍁')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002139585101'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '+oZ27l2vnexphZTVl')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002072864187')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]


                           


# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://demo-gsmz.onrender.com".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://demo-gsmz.onrender.com/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://smd-linkzz.koyeb.app/".format(FQDN)
else:
    URL = "https://smd-linkzz.koyeb.app/".format(FQDN)



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
