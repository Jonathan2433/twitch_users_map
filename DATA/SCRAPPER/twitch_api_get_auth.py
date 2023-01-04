import requests
import twitch_api_login

authURL = 'https://id.twitch.tv/oauth2/token'
Client_ID = twitch_api_login.Client_ID
Secret = twitch_api_login.Secret

AutParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }


def get_auth():
    autcall = requests.post(url=authURL, params=AutParams)
    access_token = autcall.json()['access_token']

    return access_token
