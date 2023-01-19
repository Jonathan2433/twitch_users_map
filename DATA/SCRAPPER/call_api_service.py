import requests


class Call_api_service:

    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token
        self.head = {
            'Client-ID': client_id,
            'Authorization': "Bearer " + access_token
        }
    # get the twitch id of a streamer
    def get_user_id(self, streamer):

        endpoint = 'https://api.twitch.tv/helix/users?login=' + streamer

        response = requests.get(endpoint, headers=self.head).json()

        if response['data']:
            return response['data'][0]['id']
        return 'problem with username'

    # get all the followers of the streamer
    def get_user_follows(self, id_twitch):
        endpoint = 'https://api.twitch.tv/helix/users/follows?to_id=' + id_twitch

        response = requests.get(endpoint, headers=self.head).json()

        return response

    def pagination(self, id_twitch, cursor):
        endpoint = 'https://api.twitch.tv/helix/users/follows?to_id=' + id_twitch + '&after=' + cursor

        response = requests.get(endpoint, headers=self.head).json()

        return response


    # get all streams on twitch RIGHT NOW
    def get_streams(self):
        endpoint = 'https://api.twitch.tv/helix/streams?language=fr'

        response = requests.get(endpoint, headers=self.head).json()

        return response

    # possibilité de get la langue du streamer ( en cours de stream actuellement ) ('broadcaster_language': 'fr')
    def get_channel_informations(self, twitch_id):
        endpoint = 'https://api.twitch.tv/helix/channels?broadcaster_id='+ twitch_id

        response = requests.get(endpoint, headers=self.head).json()

        return response

    def get_channel_editors(self, twitch_id):
        endpoint = 'https://api.twitch.tv/helix/channels/editors?broadcaster_id=' + twitch_id

        response = requests.get(endpoint, headers=self.head).json()

        return response

    def get_user(self, twitch_id):

        endpoint = 'https://api.twitch.tv/helix/users?id=' + twitch_id + '&scope=user%3Aedit%20user%3Aread%3Aemail'

        response = requests.get(endpoint, headers=self.head).json()

        if response['data']:
            return response['data']
        return 'problem with username'