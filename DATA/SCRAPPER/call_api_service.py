import requests


class Call_api_service:

    def __init__(self, client_id, client_secret, access_token):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.head = {
            'Client-ID': client_id,
            'Authorization': "Bearer " + access_token
        }

    def get_user_id(self, streamer):

        endpoint = 'https://api.twitch.tv/helix/users?login=' + streamer

        response = requests.get(endpoint, headers=self.head).json()

        if response['data']:
            return response['data'][0]['id']
        return 'problem with username'

    def get_user_follows(self, id_twitch):
        endpoint = 'https://api.twitch.tv/helix/users/follows?to_id=' + id_twitch

        response = requests.get(endpoint, headers=self.head).json()

        return response

    def get_streams(self):
        endpoint = 'https://api.twitch.tv/helix/streams'

        response = requests.get(endpoint, headers=self.head).json()

        return response



