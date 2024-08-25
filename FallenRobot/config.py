class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 24620300
    API_HASH = "9a098f01aa56c836f2e34aee4b7ef963"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002023182491)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://botmaker9675208:botmaker9675208@cluster0.sc9mq8b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "Anime_enigmatic"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7296057104:AAF_PCWejKOMGkcCcLvpUcxGnILFUF9S1pY"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7027685257 # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [7027685257]  # User id of sudo users
    DEV_USERS = [7027685257]  # User id of dev users
    DEMONS = [7027685257]  # User id of support users
    TIGERS = [7027685257]  # User id of tiger users
    WOLVES = [7027685257]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
