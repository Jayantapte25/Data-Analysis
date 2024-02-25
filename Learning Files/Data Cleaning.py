import pandas as pd 

raw_csv_data = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Absenteeism.csv")
df = raw_csv_data.copy()

#pd.options.display.max_columns = None - To Display full columns of CSV
#pd.options.display.max_rows = None - To Display full columns of CSV

#Dropping the ID columns
df = df.drop(['ID'], axis = 1)

print(df)

#Now there is Date Column in our Data, We will Clean that 07/07/2015
df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%Y')
print(df['Date'])

#Now we will Segregate Month & Day Column - Make it Weekwise
print(df['Date'][0].month) #this gives us month (.month - Inbuild Function)

list_month=[]
for i in df['Date']:
    month = i.month
    list_month.append(month)

df['Months'] = list_month
print(df)

#For months the count starts from 1 & for weeks the count starts from 0 :)
print(df['Date'][3].weekday())
list_week=[]
for i in df['Date']:
    month = i.weekday()
    list_week.append(month)

df['Week'] = list_week
print(df)

#Now in Education column there 4 values (1,2,3,4) (unpad 1=0), (Padha hua 2,3,4=1)
print("\nEducation Column\n",df['Education'])

print("\nCounts\n",df['Education'].value_counts())
df['Education'] = df['Education'].map({1:0, 2:1, 3:1, 4:1})

print("\nUnique Columns\n",df['Education'].unique())

#Now we will put last columns in the first
print("\nAll Columns\n",df.columns)

column_name = ['Months','Week','Reason for Absence', 'Date', 'Transportation Expense','Distance to Work', 'Age', 'Daily Work Load Average', 'Body Mass Index','Education', 'Children', 'Pets', 'Absenteeism Time in Hours']
df = df[column_name]
print("\nAfter Revolving\n",df)