import os
from dotenv import load_dotenv


load_dotenv()

MONGO_HOST = os.getenv("MONGO_HOST")
print(MONGO_HOST)
MONGO_PORT = int(os.getenv("MONGO_PORT"))
print(MONGO_PORT)
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")
MONGO_AUTH_MECHANISM = os.getenv("MONGO_AUTH_MECHANISM")