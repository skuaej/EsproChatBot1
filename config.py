from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "24411134"
# -------------------------------------------------------------
API_HASH = "da78963da6eaaf521133e00628434271"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "8410601684:AAHFIJ25M0QNLcpjuOdcDyxvmYnpJDteXNM")
STRING1 = getenv("STRING_SESSION", None)
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://oliva:oliva123@cluster0.6cohqfv.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(getenv("OWNER_ID", "7850114307"))
SUPPORT_GRP = "EsproSupport"
UPDATE_CHNL = "EsproUpdate"
OWNER_USERNAME = "Hinatahubot"
