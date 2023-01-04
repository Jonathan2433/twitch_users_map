import requests
import twitch_api_login
import twitch_api_get_auth


access_token = twitch_api_get_auth.get_auth()

head = {
    'Client-ID': twitch_api_login.Client_ID,
    'Authorization': "Bearer " + access_token
}

def get_user_id(head, streamer):

    endpoint = 'https://api.twitch.tv/helix/users?login=' + streamer

    response = requests.get(endpoint, headers=head).json()

    if response['data']:
        return response['data'][0]['id']
    return 'problem with username'


id_twitch = get_user_id(head, 'dev_optic')

print(id_twitch)
def get_user_follows(id_twitch):
    endpoint = 'https://api.twitch.tv/helix/users/follows?to_id=' + id_twitch

    response = requests.get(endpoint, headers=head).json()

    return response


print(get_user_follows(id_twitch))



