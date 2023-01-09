import csv
import call_api_service as ca
import twitch_api_login
import authenticator
import time

client_id = twitch_api_login.Client_ID
client_secret = twitch_api_login.Secret

top_2400 = []

with open('../top_2400_streamer.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        top_2400.append(', '.join(row))


auth = authenticator.Auth(client_id, client_secret)
access_token = auth.get_auth()

call_api = ca.Call_api_service(client_id, client_secret, access_token)

streamers = {}

for streamer in top_2400:
    streamer_id = call_api.get_user_id(streamer)
    streamers[streamer] = streamer_id


for streamer_id in streamers.values():
    print(call_api.get_user_follows(streamer_id))