import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6752160844:AAFkUida7_ui9eHCoglyV5HLMvts-UsajP0")
      API_ID = int(os.environ.get("APP_ID", "26322638"))
      API_HASH = os.environ.get("API_HASH","66270c65f5a0249c70cf42c8a8ebeef1")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "Join here - https://t.me/animedhaba")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "asurXOO")
