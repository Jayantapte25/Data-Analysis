filename = "C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Source.txt"

#Longer Method of Reading the file
file = open(filename, mode = 'r')
text =  file.read()
print(text)
file.close()

#Reading the file
with open(filename, mode='r') as out_file:
    text = out_file.read()
    print(text)

#Writing the file
with open(filename, mode = 'w') as out_file:
    out_file.write("Jayant & Ayush")

import pandas as pd
df = pd.read_csv('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/New.csv')
print(df)

df = pd.read_csv('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/New.csv', index_col='Name')
print(df)

location = pd.read_csv('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company.csv', usecols = ['StringID', 'Location', 'Region'], index_col='StringID')
print(location.head())

filename='C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company.csv'
location = pd.read_csv(filename, sep='\,', engine = 'python')
print(location.head())

location = pd.read_csv('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Customer-Gender.csv')
print(location.head())
print(type(location))

#Exporting data into another CSV File
location.to_csv('CSVExport.csv')

# The DataFrame represents the tabular data. If the DataFrame has only one column or row,
# you can use the "squeeze" method to reduce its # dimensions and convert it into a Series.

#Squeezing because if has only one column, We convert Dataframe to Series & it only work when we have 1 column
data = pd.read_csv('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company.csv', usecols=['Product'])

#The squeeze() function is used to convert a DataFrame or Series with a single column into a pandas Series
#This can be beneficial when you want to perform Series-specific operations, such as using Series methods, functions, or statistical calculations, on the data.
df_squeeze = data.squeeze("columns")
print(data.head())
print(type(df_squeeze))

 