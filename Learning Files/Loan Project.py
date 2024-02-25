import numpy as np
np.set_printoptions(suppress=True, linewidth=100, precision=2) 
#supress: gives clean output in numbers, Linewidth= only 100 char in one line, precision: 2 decimal points

#autostrip removes extra white columns from the data
raw_data = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/loan-data.csv", delimiter=';', skip_header = 1, autostrip=True) 
print(raw_data)

#checking the missing values in the dataset
print("\n",np.isnan(raw_data).sum()) #gives all not a number (NAN)

#here we store the mean of each column - It may give warning as our entire column might be NAN. So it can't find mean of it. 
#but actually it is not NAN, they are string values. It is stored as NAN as genfromtxt can't read strings. 
temporary_fill = np.nanmax(raw_data)+1 
print(temporary_fill)
temparary_mean = np.nanmean(raw_data, axis=0)
print(temparary_mean)

#Here we are creating 3 arrays
#1 saves min of each column
#2 gives mean value of column
#3 gives max value of column
temparary_stats = np.array([np.nanmin(raw_data, axis=0), temparary_mean, np.nanmax(raw_data, axis=0)])
print("\n\n This is Temp-Stats:\n]",temparary_stats)

#now as we can't access string values, as they are shown as NAN. So we make 2 arrays for numbers & strings
#splitting the dataset (Seperating string values)
Columns_string = np.argwhere(np.isnan(temparary_mean)).squeeze() #squeeze function converts data into 1 dimentions
print(Columns_string) #this gives all columns having strings values (NAN) because temparary_mean has mean of all columns. 

#This is storing string & numbers in different functions
loan_data_strings = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/loan-data.csv",
                                  delimiter=';',
                                  skip_header =1,
                                  autostrip= True,
                                  usecols= Columns_string,
                                  dtype = str)
print(loan_data_strings)

####################################################################################################################################

#splitting the dataset (Seperating Numeric values)
Columns_numeric = np.argwhere(np.isnan(temparary_mean) == False).squeeze()
print(Columns_numeric) #It gives places where numbers are present. Values apart from NAN. that's why False.

loan_data_numeric = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/loan-data.csv",
                                  delimiter=';',
                                  skip_header =1,
                                  autostrip= True,
                                  usecols= Columns_numeric,
                                  filling_values=temporary_fill)
print(loan_data_numeric)


#Now the we have removed Columns name as it doesn have data (Skip Header=1)(The first row). So we have to again add it. 
#We are just keeping first row (Column Names) - Skipping Footer - All row from below skipping first row :)
header_full = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/loan-data.csv",
                            delimiter=';',
                            autostrip=True,
                            skip_footer=raw_data.shape[0],
                            dtype=str)
print("\n",header_full)

#Now we don't want all columns. (We are also splitting columns names (String) (Numeric))
#Column names which has all the strings. We are storing in string_header function
#Column names which has number we are storing in header_numeric fucntion.
header_string, header_numeric = header_full[Columns_string], header_full[Columns_numeric]
print("\n",header_string,"\n","\n", header_numeric)

#############################################################################################################################################

#Creating Checkpoints:
#now while preprocessing, we change the CSV many times. So while coding we save it's multiple copies so that we don't miss the data
def checkpoint(file_name, checkpoint_header, checkpoint_data):
    np.savez(file_name, header = checkpoint_header, data = checkpoint_data)
    checkpoint_variable = np.load(file_name +".npz")
    return(checkpoint_variable)

checkpoint_test = checkpoint("C:/Users/jayan/OneDrive/Documents/Data Analytics/Exported Data", header_string, loan_data_strings)
print("\nCheckpoint\n",checkpoint_test['header'],"\n","\n", checkpoint_test['data'])

##########################################################################################################################################

#Manipulating String Columns
print("\nThe Original Columns Names:   \n", header_string)

print("\n####\n")
#1 - Manipulating First Column
header_string[0]='issue_date' #renaming the column name
print(np.unique(loan_data_strings[:,0])) #Gives only Unique Values in the column
loan_data_strings[:,0]=np.chararray.strip(loan_data_strings[:,0],"-15") #since every line has -15 common, we remove that.
print("\nWe remove -15  :",loan_data_strings[:,0])

months = np.array(['', 'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
for i in range(13):
    loan_data_strings[:,0]=np.where(loan_data_strings[:,0]==months[i],
                               i,
                               loan_data_strings[:,0])
    
print("\nWe Replace Months with Numbers\n",np.unique(loan_data_strings[:,0]))

print("\n####\n")
#2 - Manipulating Second Column
print("Column 2   :",np.unique(loan_data_strings[:,1]))
loan_type = np.array(['','(31-120 days)','Charged Off','Default']) #We replace these values (Because they are bad) with 0 & rest with 1
loan_data_strings[:,1] = np.where(np.isin(loan_data_strings[:,1],loan_type),0,1) #use this to seperate 1,0
print("\nAfter Reaplce:  ",np.unique(loan_data_strings[:,1]))

print("\n####\n")
#3 - Manipulating Third Column
print("Column 3   :",np.unique(loan_data_strings[:,2]))
loan_data_strings[:,2]=np.chararray.strip(loan_data_strings[:,2]," months") #removing redundant 'month' from all lines.
print(np.unique(loan_data_strings[:,2])) #But there are still empty spaces in the column. So now we will remove them.

loan_data_strings[:,2] = np.where(loan_data_strings[:,2]=='',60,loan_data_strings[:,2])
print(np.unique(loan_data_strings[:,2])) #So we successfully removed '' Empty Space. 

print("\n####\n")
#4 - Manipulating Fourth Column
print("\nBefore Removing :  ",header_string,"\n") 
header_string = np.delete(header_string, 3)
loan_data_strings = np.delete(loan_data_strings, 3, axis=1)
header_string = np.delete(header_string, 3)
loan_data_strings = np.delete(loan_data_strings, 3, axis=1)
print("After Removing :  ",header_string)

print("\n####\n")
#5 - Manipulating Fivth Column
# Since we deleted 2 columns, We are using 3 again
#Source verified & Verified = 1 & others be 0
print("Column 5   :",np.unique(loan_data_strings[:,3]))
loan_data_strings[:,3] = np.where((loan_data_strings[:,3]=='') | (loan_data_strings[:,3]=='Not Verified'),0,1)
print(np.unique(loan_data_strings[:,3]))

print("\n####\n")
#6 - Manipulating sixth Column
print(loan_data_strings[:,4])
loan_data_strings[:,4] = np.chararray.strip(loan_data_strings[:,4], "https://www.lendingclub.com/browse/loanDetail.action?loan_id=")
print("\n After removing  :",loan_data_strings[:,4].astype(dtype = np.int32))

#Now the remaining number in the URL is similar to the ID, which is not in string. It is in header_numeric function.
print("\n",loan_data_numeric[:,0].astype(dtype = np.int32)) 
print("\n",np.array_equal(loan_data_numeric[:,0].astype(dtype = np.int32), loan_data_strings[:,4].astype(dtype = np.int32))) 
#So we combine 2 duplicate columns

print("\n",loan_data_strings)
loan_data_strings = np.delete(loan_data_strings,4,axis=1)
print("\n",loan_data_strings)

print("\n",header_string)
header_string = np.delete(header_string,4)
print("\n",header_string)

print("\n####\n")
#7 - Manipulating seventh Column
print(np.unique(loan_data_strings[:,4]))
states_names, states_count = np.unique(loan_data_strings[:,4], return_counts= True)
print("\n",states_count) #this gives us number of time value is repeated.

#Now we will sort the array & it's coresponding values
states_count_sorted = np.argsort(-states_count) #argsort doesn't sort but gives it's position
print("\n\n", states_names[states_count_sorted],"\n\n",states_count[states_count_sorted])

#Now we will mark 0 for null values & categorise states into different groups
loan_data_strings[:,4] = np.where(loan_data_strings[:,4] == '', 0, loan_data_strings[:,4])
states_west = np.array(['CA', 'NY', 'TX', 'FL', 'IL', 'NJ', 'GA', 'PA', 'OH', 'MI', 'NC', 'VA', 'MD', 'AZ'])
states_east = np.array(['WA', 'MA', 'CO', 'MO', 'MN', 'NH', 'NM', 'WV', 'HI'])
states_south = np.array(['IN', 'WI', 'CT', 'TN', 'NV', 'AL', 'LA', 'OR', 'SC', 'KY', 'KS', 'OK', 'UT', 'AR', 'MS'])
states_north = np.array(['RI', 'MT', 'DE', 'DC', 'WY', 'AK', 'NE', 'SD', 'VT', 'ND', 'ME'])

loan_data_strings[:,4] = np.where(np.isin(loan_data_strings[:,4], states_west), 1, loan_data_strings[:,4])
loan_data_strings[:,4] = np.where(np.isin(loan_data_strings[:,4], states_east), 2, loan_data_strings[:,4])
loan_data_strings[:,4] = np.where(np.isin(loan_data_strings[:,4], states_south), 3, loan_data_strings[:,4])
loan_data_strings[:,4] = np.where(np.isin(loan_data_strings[:,4], states_north), 4, loan_data_strings[:,4])

print("\nAll Unique Values : \n",np.unique(loan_data_strings[:,4])) #putting all the states into 4 categories & into 1,2,3,4.

loan_data_strings = loan_data_strings.astype(np.int32)
print(loan_data_strings) #now we have converted all string values to numeric.

#Creating a checkpoint 
checkpoint_string = checkpoint("C:/Users/jayan/OneDrive/Documents/Data Analytics/Exported Data", header_string, loan_data_strings)

#######################################################################################################################################

#Manipulating Numeric Columns
print("\nThe Original Columns Names:   \n", header_numeric)

#Columns: ['id' 'loan_amnt' 'funded_amnt' 'int_rate' 'installment' 'total_pymnt']
#Now we store mean value for Funded_amount & Max amount for rest of the value in place of empty values.
#Header_Numeric doesn't contain any nul values as we have replaced it 'filling_values=temparary_fill).
#So we will replace all the max values with mean values in Funded_amount.

#This temp stats information is important here
#Here we are creating 3 arrays
#1 saves min of each column
#2 gives mean value of column
#3 gives max value of column

#1 - Replacing Funded_Amnt column
loan_data_numeric[:,2] = np.where(loan_data_numeric[:,2] == temporary_fill,
                                  temparary_stats[0, Columns_numeric[2]], #Here 0 indicates first column from stats which has min values
                                  loan_data_numeric[:,2])
print("\nAfter Sorting:  ",loan_data_numeric[:,2])

#2 - Replacing Interest Rate, Total Payment, Installment column
for i in [1,3,4,5]:
    loan_data_numeric[:,i] = np.where(loan_data_numeric[:,i] == temporary_fill,
                                  temparary_stats[2, Columns_numeric[i]], #Here 0 indicates first column from stats which has max values.
                                  loan_data_numeric[:,i])
print("\nAfter Sorting: \n",loan_data_numeric) 

loan_data_numeric = loan_data_numeric.astype(dtype=np.float32).astype(dtype=np.int32) #Converting Float values to INT
print("\nAfter Converting:  \n",loan_data_numeric) 

checkpoint_numeric = checkpoint("Checkpoint-Numeric", header_numeric, loan_data_numeric)

###############################################################################################

#Now we will combine the 2 seperated CSV's (Strings) (Numeric)
print("\n",checkpoint_string['data'].shape) #(10000, 5)
print("\n",checkpoint_numeric['data'].shape) #(10000, 6)

#joining 2 CSV's
loan_data = np.hstack((checkpoint_numeric['data'], checkpoint_string['data']))
print("\n This Joined CSV contain These many NAN's: ",np.isnan(loan_data).sum())
print("\n",loan_data) 

#Now joining the 2 Columns names as we joined them (String & Numeric)
header_full = np.concatenate((checkpoint_numeric['header'], checkpoint_string['header']))
print("\n",header_full)

#First columns is ID, So we will sort the whole CSV accoding to this ID
loan_data = loan_data[np.argsort(loan_data[:,0])]
print("\nSorting Acc to ID Column\n",loan_data)

#Merging Header (Column Names with Rest numeric data) (This will auto convert INT to Text)
loan_data = np.vstack((header_full,loan_data))
print("\nMerging with column name\n",loan_data)

#Now we will store all this Bandi-Rona in CSV File
np.savetxt("loan-data-Prepocessed.csv",
           loan_data,
           fmt="%s",
           delimiter=',')