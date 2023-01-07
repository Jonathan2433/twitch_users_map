import requests


class Auth:

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.autParams = {'client_id': self.client_id,
                     'client_secret': client_secret,
                     'grant_type': 'client_credentials'
                     }
        self.url = 'https://id.twitch.tv/oauth2/token'

    def get_auth(self):
        autcall = requests.post(url=self.url, params=self.autParams)
        access_token = autcall.json()['access_token']

        return access_token


