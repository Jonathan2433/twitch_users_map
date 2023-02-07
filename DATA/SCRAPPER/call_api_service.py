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
        endpoint = 'https://api.twitch.tv/helix/users/follows?to_id=' + id_twitch + '&first=100'

        response = requests.get(endpoint, headers=self.head).json()

        # total_followers = response['total']
        followers_data = response['data']
        cursor = response['pagination']['cursor']

        followers = {}
        for follower in followers_data:
            follower_pseudo = follower['from_name']
            follower_twitch_id = follower['from_id']
            followers[follower_pseudo] = follower_twitch_id

        while(cursor):
            endpoint_pagination = 'https://api.twitch.tv/helix/users/follows?to_id=' + id_twitch + '&first=100' + '&after=' + cursor

            response_pagination = requests.get(endpoint_pagination, headers=self.head).json()

            followers_data_pagination = response_pagination['data']

            for follower_pagination in followers_data_pagination:
                follower_pseudo_pagination = follower_pagination['from_name']
                follower_twitch_id_pagination = follower_pagination['from_id']
                followers[follower_pseudo_pagination] = follower_twitch_id_pagination

            if 'cursor' in response_pagination['pagination']:
                cursor = response_pagination['pagination']['cursor']

            else:
                return followers

        return followers

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



import authenticator
import twitch_api_auth

client_id = twitch_api_auth.Client_ID
secret = twitch_api_auth.Secret

auth = authenticator.Auth(client_id, secret)
access_token = auth.get_auth()

ca = Call_api_service(client_id, access_token)

dev_optic_id = ca.get_user_id('Squeezie')

followers = ca.get_user_follows(str(dev_optic_id))

print(followers)
print(len(followers))