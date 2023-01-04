import requests
import twitch_api_auth

authURL = 'https://id.twitch.tv/oauth2/token'
Client_ID = twitch_api_auth.Client_ID
Secret = twitch_api_auth.Secret

AutParams = {'client_id': Client_ID,
             'client_secret': Secret,
             'grant_type': 'client_credentials'
             }


def get_user_id(streamer):

    autcall = requests.post(url=authURL, params=AutParams)
    access_token = autcall.json()['access_token']

    head = {
        'Client-ID': Client_ID,
        'Authorization': "Bearer " + access_token
    }

    URL = 'https://api.twitch.tv/helix/users?login=' + streamer

    response = requests.get(URL, headers=head).json()['data'][0]

    return response['id']



print(get_user_id('papesan'))
#%%
