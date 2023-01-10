import call_api_service as ca
import twitch_api_login
import authenticator

client_id = twitch_api_login.Client_ID
client_secret = twitch_api_login.Secret

auth = authenticator.Auth(client_id, client_secret)
access_token = auth.get_auth()

call_api = ca.Call_api_service(client_id, access_token)

streamer_id = call_api.get_user_id('dev_optic')

print(streamer_id)
dev_optic_followers = call_api.get_user_follows(streamer_id)

print(dev_optic_followers)

# todo faire une boucle qui parcours ma liste des 2500 streamers, pour chaque streamer, faire l'apel d'apî pour recup son ID_twitch ET stocker cet id sur notre csv
#  et ensuite refaire un appel d'api pour récup ses followers

