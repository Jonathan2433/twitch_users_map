import requests
from bs4 import BeautifulSoup

url = "https://twitchtracker.com/channels/ranking/french"
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'})

soup = BeautifulSoup(page.content, "html.parser")

# Récupère tous les éléments de la liste
streamer_elements = soup.find_all("td")

for a in soup.find_all('a', href=True):
    print (a['href'])




# Pour chaque élément de la liste, récupère le pseudo du streamer
# for streamer_element in streamer_elements:
#     username = streamer_element.find("a").getText()
#     print(username)