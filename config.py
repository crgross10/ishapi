import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Settings(BaseSettings):
    auth_url_spotify: str
    client_id: str
    client_secret: str
    base_url_spotify: str
    id_party: str
    id_pop: str
    id_rock: str
    id_classic: str

@lru_cache()
def get_settings():
    return Settings(
        auth_url_spotify = os.environ["AUTH_URL_SPOTIFY"],
        client_id =os.environ["CLIENT_ID"],
        client_secret = os.environ["CLIENT_SECRET"],
        base_url_spotify = os.environ["BASE_URL_SPOTIFY"],
        id_party = os.environ["ID_PARTY"],
        id_pop = os.environ["ID_POP"],
        id_rock = os.environ["ID_ROCK"],
        id_classic = os.environ["ID_CLASSIC"],
    )
