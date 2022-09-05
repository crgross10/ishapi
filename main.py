from fastapi import FastAPI
import requests
import json 
import os
from config import get_settings


settings = get_settings()
app= FastAPI()

@app.get("/")
def home():
    return "Hello world!"

@app.get("/playlist")
def playlist(city: str=None, lat: str=None, lon: str=None):
    if not city and not lat and not lon:
        return {'detail': 'Você deve informar uma cidade ou as coordenadas.'}
    
    if not city and lat and not lon:
        return {'detail': 'Você deve informar a latitude e a longitude ou a cidade.'}
    
    if not city and not lat and lon:
        return {'detail': 'Você deve informar a latitude e a longitude ou a cidade.'}
    
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&lat={lat}&lon={lon}&units=metric&appid=b77e07f479efe92156376a8b07640ced'
    response = requests.get(url)
    data = response.json()
    
    if data['sys']['country'] == 'IT':
        return {'detail': 'Não foi possivel localizar a playlist. Verifique os dados informados!'}

    return get_list_musics(data['main']['temp'])

def get_access_token():
    AUTH_URL = settings.auth_url_spotify
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': settings.client_id,
        'client_secret': settings.client_secret
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token

def get_list_musics(temperature):
    tracks={}
    token = get_access_token()   
    BASE_URL = settings.base_url_spotify
    headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
        }
    
    if temperature >=30:
        id_tracks=settings.id_party
    elif temperature >15 and temperature < 30:  
        id_tracks=settings.id_pop
    elif temperature > 9 and temperature < 15:  
        id_tracks=settings.id_rock
    else:
        id_tracks=settings.id_classic 
    
    response = requests.get(BASE_URL + f'playlists/{id_tracks}/tracks' , headers=headers)
    data = response.json()
    items = data['items']
  
    for i in items:
        if isinstance(i, dict):
            for key, value in i.items():
                if key=='track':
                    tracks.update({value['name'] : value['external_urls']['spotify']})
    
    return tracks                