import pandas as pd 
import json

#So in this code we are converting Json files intro CSV files.

#Match Results
with open('C:/Users/jayan/OneDrive/Documents/Power BI/Cricket Analytics/t20_json_files/t20_wc_match_results.json') as f:
    data =  json.load(f)

df = pd.DataFrame(data[0]['matchSummary']) #now we are storing it in a Pandas Dataframe. Check json file to know why data[0] is used.
print("\n\nMatch Results \n\n",df)

df.rename({'scorecard': 'match_id'}, axis=1, inplace=True) #So we rename it for better understanding.
print(df.head())

#Batting Summary
with open('C:/Users/jayan/OneDrive/Documents/Power BI/Cricket Analytics/t20_json_files/t20_wc_batting_summary.json') as f:
    data1 =  json.load(f)

    array_df = []
    for rec in data1:
        array_df.extend(rec['battingSummary']) #here we use loop because we have multiple records in the json file.

df1 = pd.DataFrame(array_df)
print("\n\nBatting Summary \n\n",df1) 

#IMPORTANT
#So because we don't have out/notout data so we use lamda function to change it to 0 & 1 (dismissal is black where it's out)
#we can also do this using replace function

df1["OUT"]=df1.dismissal.apply(lambda x: "out" if len(x)>0 else "not out")
df1.drop(['dismissal'], axis=1, inplace=True)
print(df1.head(15))

df1['batsmanName'] = df1['batsmanName'].apply(lambda x: x.replace('á€', '')) #So some players had information in different language so we use this to remove it.
df1["batsmanName"] = df1['batsmanName'].apply(lambda x: x.replace('\xae', ''))
print(df1.head(15))

#Bowling Summary
with open('C:/Users/jayan/OneDrive/Documents/Power BI/Cricket Analytics/t20_json_files/t20_wc_bowling_summary.json') as f:
    data2 =  json.load(f)

    array_df = []
    for rec in data2:
        array_df.extend(rec['bowlingSummary'])#same case with bowling summary

df2 = pd.DataFrame(array_df)
print("\n\nBowling Summary \n\n",df2)

#Player Stats
with open('t20_json_files/t20_wc_player_info.json') as f:
    data = json.load(f)

df_players = pd.DataFrame(data)#here we don't use loop because we have only one record in the json file.

print(df_players.shape) #Finally we also convert player stats into csv file.
df_players.head(10)