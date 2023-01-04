import requests
import twitch_api_auth
import twitch_api_get_auth

def get_user_id(access_token, streamer):

    head = {
        'Client-ID': twitch_api_auth.Client_ID,
        'Authorization': "Bearer " + access_token
    }

    endpoint = 'https://api.twitch.tv/helix/users?login=' + streamer

    response = requests.get(endpoint, headers=head).json()

    if response['data']:
        return response['data'][0]['id']
    return 'problem with username'


access_token = twitch_api_get_auth.get_auth()

print(get_user_id(access_token, 'dev_optic'))



# https://api.twitch.tv/helix/users/follows?to_id=23161357'
#%%
