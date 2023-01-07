import call_api_service as ca
import twitch_api_login
import authenticator

client_id = twitch_api_login.Client_ID
client_secret = twitch_api_login.Secret

auth = authenticator.Auth(client_id, client_secret)
access_token = auth.get_auth()

call_api = ca.Call_api_service(client_id, client_secret, access_token)

dev_optic_id = call_api.get_user_id('domingo')

dev_optic = call_api.get_user_follows(dev_optic_id)

print(dev_optic)

streams = call_api.get_streams()

print(streams)