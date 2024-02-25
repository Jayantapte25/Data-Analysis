import requests
base_url = "https://itunes.apple.com/search"
url = base_url + "?term=Emiway+Bantai&country=IN"
response = requests.get(url)

print(response.ok) #prints True
print(response.status_code) #prints 200 
print(response.url) #prints URL
print(response.content)

import json
print(json.dumps(response.json(), indent = 4))
print(response.json().keys())

info = response.json()
import pandas as pd
songs_df = pd.DataFrame(info["results"])
print(songs_df)

#This code creates CSV Files after RUN 
# songs_df.to_csv("songs_info.csv")
# songs_df.to_excel("songs_info.xlsx")
