import call_api_service as ca
import twitch_api_login
import authenticator

client_id = twitch_api_login.Client_ID
client_secret = twitch_api_login.Secret

auth = authenticator.Auth(client_id, client_secret)
access_token = auth.get_auth()

call_api = ca.Call_api_service(client_id, access_token)

dev_optic_id = call_api.get_user_id('datalgo')

# dev_optic_followers = call_api.get_user_follows(dev_optic_id)

# print(dev_optic_followers)

streams = call_api.get_streams()

print(streams)
# channel_informations = call_api.get_channel_informations(dev_optic_id)
#
# print(channel_informations)

# channel_editors = call_api.get_channel_editors(dev_optic_id)
#
# print(channel_editors)
#
# get_user = call_api.get_user(dev_optic_id)
#
# print(get_user)