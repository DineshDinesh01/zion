import pyrebase

from core.db.fire_base import config

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()
