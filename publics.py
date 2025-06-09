from dotenv import load_dotenv
import os
import hashlib

load_dotenv()


def db():
    from pymongo import MongoClient
    con = MongoClient(Settings.MONGO_URL)
    return con[Settings.DB_NAME]


def get_str_hash(string: str) -> str:
    text_encoded = string.encode('utf-8')
    hashed_text = hashlib.sha256(text_encoded).hexdigest()
    return hashed_text


def get_array_hash(array: list):
    array_string = ''.join(map(str, array))
    array_bytes = array_string.encode('utf-8')
    hash_object = hashlib.sha256(array_bytes)
    return hash_object.hexdigest()


class Settings:
    MONGO_URL = os.environ.get('MONGO_URL')
    PROJECT_PATH = os.environ.get('PROJECT_PATH')
    DB_NAME = os.environ.get('DB_NAME')
    DB_NAME_TEST = os.environ.get('DB_NAME_TEST')
    DEV_MODE = os.environ.get('DEV_MODE')
    SHOW_TOKEN = os.environ.get('SHOW_TOKEN') == 'True'
