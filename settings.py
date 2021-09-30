from decouple import config

APIKEY = config("APIKEY")
BASE_URL = config("BASE_URL", "https://www.alphavantage.co/query")