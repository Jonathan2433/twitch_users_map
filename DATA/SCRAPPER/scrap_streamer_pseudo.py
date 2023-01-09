import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


streamers = []

def scrap_top_2500():
    for i in range(1, 51):
        url = "https://twitchtracker.com/channels/ranking/french?page=" + str(i)
        print(f"je request actuellement {url}")

        request = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'})

        soup = BeautifulSoup(request.content, "html.parser")

        # Récupère tous les éléments de la liste
        streamer_elements = soup.select("td:nth-child(3) > a")

        for pseudo in streamer_elements:
            print(f"j'enregistre actuellement le streamer : {pseudo.get_text(strip=True)}")
            streamers.append(pseudo.get_text(strip=True))
            time.sleep(0.05)

    return streamers

streamers = scrap_top_2500()

print(len(streamers))

#transform list to dataframe
df = pd.DataFrame(streamers)

# saving the dataframe
df.to_csv('../top_2500_streamer.csv', index=False, header=False)



