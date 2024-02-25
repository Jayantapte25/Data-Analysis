import numpy as np

lending_co_data_numeric = np.loadtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric.csv", delimiter=',')
print(np.isnan(lending_co_data_numeric)) #isnan not a number

lending_co_data_numeric_nan = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric-NAN.csv", delimiter=';')
print("\n",np.isnan(lending_co_data_numeric_nan))

#Now we want to fill the missing values with something which is not a part of our dataset
#So we first find max element & fill this at missing places.

temporary_fill = np.nanmax(lending_co_data_numeric_nan).round(2)+1 #puts 2 decimal points & adds 1 to it.
print("\n",temporary_fill)

print("\n This line ON")
lending_co_data_numeric_nan = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric-NAN.csv", delimiter=';', filling_values=temporary_fill) #filling_values automatically finds missing values & here were replacing it with maxvalue.
print(np.isnan(lending_co_data_numeric_nan).sum()) #sum counts the number of true values.

#Filling missing values with Mean of their column
lending_co_data_numeric_man = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric-NAN.csv", delimiter=';') 

#Here we find mean of first column & we get value as 2250
#np.nanmean() calculates the mean while ignoring NaN values
#axis=0 argument specifies that the calculation is done along the columns
temporary_mean = np.nanmean(lending_co_data_numeric_man, axis=0).round(2)
print("\nMean-1st-column",temporary_mean[0])

#now here we store mean of whole table = 64002
temporary_fill = np.nanmax(lending_co_data_numeric_man).round(2)+1
print("Max Value",temporary_fill)

#Now we add this new temporary_fill in missing spaces in CSV, & it store max value of whole table
lending_co_data_numeric_man = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric-NAN.csv", delimiter=';',filling_values=temporary_fill)
print(np.mean(lending_co_data_numeric_man[:,0]).round(2))

#What is [:,0] specify?
#The colon : in the first position indicates that you want to include all rows of the array. This is used to specify the range of rows you want to select. In this case, it means you want to include all rows.
#The 0 in the second position specifies the column index. This means you want to select all elements from the first column of the array.

#So because we added max value of whole table in column 1, the mean of column 1 increased from 2250 to 4263 which is wrong
#Correct method is to store mean of the column in the spaces of their respective columns.

#Here we store mean value in the first column, in the empty spaces in the first column & we get 2250. Correct Value
#what 3 argurment of where function suggests:
#1st it checks for max value from Temporary_fill, because we already replaced it above. Than in 2nd it replaces it with Temp_mean[0] means of the 0th column
lending_co_data_numeric_man[:,0] = np.where(lending_co_data_numeric_man[:,0] == temporary_fill, temporary_mean[0], lending_co_data_numeric_man[:,0])
print(np.mean(lending_co_data_numeric_man[:,0]).round(2))
print()

#here we store mean value of each column in their respective empty spaces
for i in range(lending_co_data_numeric_man.shape[1]):
    lending_co_data_numeric_man[:,i] = np.where(lending_co_data_numeric_man[:,i] == temporary_fill, temporary_mean[i], lending_co_data_numeric_man[:,i])
    print("Mean: ",np.mean(lending_co_data_numeric_man[:,i]).round(2))

#Removing Values & in this we delete the first column of the CSV with =0
lending_co_data_delete = np.loadtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric.csv", delimiter=',')
print(np.delete(lending_co_data_delete, 0))

#Removing the first row of the CSV
print("\n",lending_co_data_delete)
print("\n",np.delete(lending_co_data_delete,0, axis=0))

#Now we will remove 1st, 2nd, 4th & Axis=0 means rows & Axis=1 means columns
print("\n",np.delete(lending_co_data_delete,[0,2,4], axis=1))

#here we delete columns & Rows simultenously (-1 deletes last row)
print("\n",np.delete(np.delete(lending_co_data_delete,[0,2,4], axis=1),(0,2,-1), axis=0))

#Sorting Values in the CSV
sort1 = np.loadtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric.csv", delimiter=',' )
print("Sorted CSV\n",np.sort(sort1))
print(np.sort(sort1[:,3])) #you can even sort single row of the CSV

#Argsort sort the CSV with Indices (1,3,0,4,5)
print("\nArg Sort Starts")
print("\n",np.argsort(sort1))
print("\n",np.argsort(sort1, axis=0))

#Argwhere check with conditions (like here is gives data from CSV having 0)
#Argwhere also gives a 2D array with row & column cordinates
print("\nArgwhere\n",np.argwhere(sort1))

#Filling missing values in CSV with Argwhere function
lending_co_data_numeric_lan = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric-NAN.csv", delimiter=';')
print("\n",lending_co_data_numeric_lan)

#Gives Cordinates of missing values
print("\nDivine\n", np.argwhere(np.isnan(lending_co_data_numeric_lan))[:5]) #head() doesn't work here because it is Pandas only, this is new style [:5]
print("\n Divine 2nd\n",lending_co_data_numeric_lan[11])

#j[0] represents the row index of the current iteration.
#j[1] represents the column index of the current iteration.
#Using this for Loop we will fill all the missing places with 0
for j in np.argwhere(np.isnan(lending_co_data_numeric_lan)):
    lending_co_data_numeric_lan[j[0], j[1]] = 0
print("\nKoshish\n",lending_co_data_numeric_lan[12])

#Casting NDarrays (Changing the data type from string to float to Int) - AS we can't directly convert from string to int
#We can also use np.genfromtxt & it will work similarly
#After this line, the casting array contains the same values as before, but they are now represented as strings instead of numbers.
casting = np.loadtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric.csv", delimiter=',')
casting = casting.astype(dtype = str)
print("\nJaari\n",casting)

#Now converting from String to float to Integer
print(casting.astype(dtype=np.float32).astype(dtype=np.int32))

#stripping - We can edit text or values in CSV
lending_co_total_price = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Total-Price.csv", delimiter=',', dtype=str, skip_header=1, usecols=[1,2,4])
print("\nResh\n",lending_co_total_price)

#Removing the text part - We successfully deleted (Id_, Product, Location) from all columns
lending_co_total_price[:,0] = np.chararray.strip(lending_co_total_price[:,0], "id_")
lending_co_total_price[:,1] = np.chararray.strip(lending_co_total_price[:,1], "Product ")
lending_co_total_price[:,2]= np.chararray.strip(lending_co_total_price[:,2], "Location")
print("\nStripping\n",lending_co_total_price)

#Now we will change the Values using Np.where - Will change from Product A to Product 1 & Product B to Product 2
#The second Argument in the where function is for false function if 'A' doesn't exist.
lending_co_total_price[:,1] = np.where(lending_co_total_price[:,1] == 'A', 1, lending_co_total_price[:,1])
lending_co_total_price[:,1] = np.where(lending_co_total_price[:,1] == 'B', 2, lending_co_total_price[:,1])
lending_co_total_price[:,1] = np.where(lending_co_total_price[:,1] == 'C', 3, lending_co_total_price[:,1])
lending_co_total_price[:,1] = np.where(lending_co_total_price[:,1] == 'D', 4, lending_co_total_price[:,1])
lending_co_total_price[:,1] = np.where(lending_co_total_price[:,1] == 'E', 5, lending_co_total_price[:,1])
print("\n",lending_co_total_price)

#Joining 2 CSV File elements using Concaternate function
x = np.loadtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric.csv", delimiter=',')
y = np.loadtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Caasting.csv", delimiter=',')
print("\nLast Part\n",np.concatenate((x, y), axis = 1)) #The axis=1 argument specifies that you want to concatenate the arrays along the horizontal axis (columns

#Finding Unique values & how many times they have appreared in the CSV
lending_co_data_numeric = np.loadtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-company-Numeric.csv", delimiter=',')
print("\n",np.unique(lending_co_data_numeric[:,1], return_counts = True))