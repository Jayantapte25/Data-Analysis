import pandas as pd
import numpy as np

# Creating a Series
print("\nCreating a Series")
product = ['F','U','C','K']
P=pd.Series(product)
print(P)
print("Size:", P.size)

P.name="PC"
print(P)

number = pd.Series([15, 1000, 23, 2, 444])
print(number.sort_values())
print(number.sort_values(ascending=False))

Sees ={'A': 20, 'B': 30, 'C': 40, 'D': 50}
A=pd.Series(Sees)
print(A)
print(A.index)

#Methods
print("\nMethods")
start = pd.Series({
    '7/4/2014': 2000,
    '1/3/2015': 1850,
    '4/17/2016': 2200,
    '9/8/2017': 1650,
    '5/21/2018': 1950,
    '11/9/2019': 2050,
    '7/30/2020': 2300,
    '12/12/2021': 1750,
    '6/5/2022': 2150,
    '2/18/2023': 2400,
    '8/22/2024': 1900,
})

print(start.head()) #Gives first 5 rows, Oftenly used to know the dataset by the progammers
print(start.sum())
print(start.min())
print(start.max()) #Gives the Max Value
print(start.idxmax())


#Data Frames
print("\nData Frames")
array_a = np.array([[3,4,1], [7,5,4]])
print(array_a)
print(pd.DataFrame(array_a))

data = {'ProductName':['P1','P2','P3','P4'], 'ProductPrice':[22,2352,352,23]}
df = pd.DataFrame(data, index =['A', 'B', 'C', 'D']) #by writing index here 0,1,2,3 get replaced with A,B,C,D
print(df)

print("\nImport CSV Starts")
data = pd.read_csv('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-Company.csv', index_col = 'LoanID')
lending_co_data = data.copy()
print(lending_co_data.head())

print("\nLine 62\n",lending_co_data.Location.head()) #gives only one column with index_col
print("\nLine 63\n", lending_co_data[['Location', 'Product']].head()) #another way to re-present values

print("\nLine 65\n", lending_co_data.index) #printing in Array format
print("\nLine 66\n", lending_co_data.columns) #printing in Array format
print(lending_co_data.dtypes)

#Merging 2 Data Frames
df1 = pd.DataFrame({'ID':[1,2,3,5,9],
                    'Col_1':[1,2,3,4,5],
                    'Col 2':[6,7,8,9,10],
                    'Col_3':[11,12,13,14,15],
                    'Col_4': ['apple', 'orange', 'banana', 'strawberry', 'raspberry'] }) 

df2 = pd.DataFrame({'ID':[1,1,3,5],
                    'Col_A': [8,9,10,11],
                    'Col_B':[12,13,15,17],
                    'Col_4': ['apple', 'orange', 'banana', 'kiwi']})

inner = pd.merge(df1, df2) #So here it found common columns from 2DF & merged them only.
print("\nMerge DataFrame\n", inner)

print("\nMerge DF on ID\n", pd.merge(df1, df2, on='ID')) #Here we are only merging on ID Column - You can also add 2-3 columns here.

#Outer Join - Takes all data from both.
print("\nOuter Join\n", pd.merge(df1, df2, on='Col_4', how='outer', suffixes=['_l','_r']))

#Left Join - Takes all data from left & common data
print("\nLeft Join\n", pd.merge(df1, df2, on='Col_4', how='left', suffixes=['_l','_r']))

#Right Join - Takes all data from right & common data
print("\nRight Join\n", pd.merge(df1, df2, on='Col_4', how='right', suffixes=['_l','_r']))

#printing certain row & column like we do in DBMS - .iloc()
#[Row value, Column Value]
print()
print("\nLine 71\n",lending_co_data.iloc[1]) #Only prints second row
print("\nLine 72\n",lending_co_data.iloc[1, 3]) #2nd row & 4th column
print("\nLine 73\n",lending_co_data.iloc[1,:])#full 2nd row
print("\nLine 74\n",lending_co_data.iloc[:,3])#full 4th Column
print("\nLine 75\n",lending_co_data.iloc[[1, 3], :])
print("\nLine 76\n",lending_co_data['TotalPrice'].iloc[2])
print("\nLine 77\n",lending_co_data['TotalPrice'].iloc[[0, 5]])

#Printing selective Rows - .loc()
print()
data = pd.read_csv('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-Company.csv', index_col = 'StringID')
lending_loc_data = data.copy()
print(lending_loc_data.head())

print("\nLine 86\n",lending_loc_data.loc['LoanID_3'])
print("\nLine 87\n",lending_loc_data.loc['LoanID_3', 'Region'])


#Text Formating
print("\n Text Formating")
operation_kpis = pd.Series(["Employee chod", "Employee madar"])
print(operation_kpis[0].lstrip('Employee')) #removes first letter from left, for right - .rstrip()

test_series = pd.Series(['Test_data', '34'])
print(test_series.str.lstrip('Test_'))

house_price = pd.Series(['$400', '$500', '$600'])
print(house_price.str.contains("$"))

time_horizon = 1, 3, 4
products = ['product 1', 'product 2']

print('Gand tuzi {} barobar for {}'.format(time_horizon[1], products[1]))


#Sorting & adding Index
print("\nSorting & adding Index")
data = pd.read_csv('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Location.csv')
location_data = data.copy()
print(location_data.head())

print("\nLine 113")
print(location_data.describe())

#adding A column Name for Index
location_data.index.name = 'index'
print("\nLine 118",location_data.head()) #also .tail() gives last 5 rows

Resh = location_data.sort_values(by='Location', ascending=False).head()
print("\nLine 118",Resh.index.sort_values())

#converting into Numpy array which are faster
print(location_data.index.to_numpy())

#Group By function, where all the rows data is manipulated according to this column data
#now other columns will be changed according 'Make' column mean.

#pricedcars.groupby(['Make']).mean()
#pricedcars.groupby(['make','body_style']).mean().head(5)




