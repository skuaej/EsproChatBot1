from pymongo import MongoClient

import config

Ritikdb = MongoClient(config.MONGO_URL)
Ritik = Ritikdb["RitikDb"]["Ritik"]


from .chats import *
from .users import *
