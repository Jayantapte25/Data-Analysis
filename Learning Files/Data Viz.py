import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# #1 - Making Bar Chart
# df_cars = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/bar_chart_data.csv")
# print(df_cars)

# #Increasing the distance between the text to avoid overlap
# plt.figure(figsize = (9,6))

# #X means X-axis & hieght means Y-axis & adding different colors.
# plt.bar(x = df_cars["Brand"], height=df_cars["Cars Listings"], color=['r','g','b','w','y','m','c']) #These are shortcuts for colors.
# plt.xticks(rotation = 45, fontsize = 13) #text on X-axis
# plt.yticks(fontsize = 13) #text on Y-axis

# #Now we will put a title to our graph (X & Y Axis)
# plt.title("Cars Listing By Brand", fontsize = 16, fontweight = "bold") #The main title above
# plt.ylabel("Number of Listing", fontsize=13, fontweight = "bold") #The vertical title alongside Y-axis
# plt.show()

# #Now this code is to save our graph as Png - But we won't need it
# plt.savefig("Used-Car.png")

#####################################################################################################

# #2 - Making Pie Chart 
# sns.set_palette('colorblind') #setting default library of colours

# df_engine = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/pie_chart_data.csv")
# print(df_engine)

# plt.figure(figsize=(10,8)) 

# plt.pie(df_engine['Number of Cars'],
#         labels = df_engine['Engine Fuel Type'].values,
#         autopct='%.2f%%', ##This gives % value of each segment inside Pie chart
#         textprops = {'size': 'x-large', #This is Extra-Large
#                      'fontweight': 'bold',
#                      'rotation': 30, 
#                      'color': 'w'}) #also all this is for text inside Pie Chart
# plt.legend()
# plt.title("Cars by Engine Fuel Type", fontsize = 18, fontweight = "bold")
# plt.show()

################################################################################################

#3 - Making Area Chart (Stacked)
# sns.set_style("white") #changes the default background to white
# sns.despine() #this removes the black border around the chart

# #this chart is specially used to depict trends
#There should be atleast 3 or more data to create this chart & also useful when we have more than 6 categories.
#Useful to depict time data (Historic) & Y Cordinates must starts from 0

# df_fuel = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/stacked_area_chart_data.csv")
# print(df_fuel)

# plt.figure(figsize=(12,6)) #dimentions of the whole chart

# colors=["#011638","#7e2987","red"]
# labels = ["Diesel", "Petrol", "Gas"]
# plt.stackplot(df_fuel['Year'], #these are columns from the CSV file.
#               df_fuel['Diesel'], #Choose wisely which column should be the base of the chart
#               df_fuel['Petrol'],
#               df_fuel['Gas'],
#               colors=colors,
#               edgecolor = 'none') #there is default edge between 2 colors

# plt.xticks(rotation = 45, fontsize = 13) #text on x-axis
# plt.ylabel("Number of Cars", fontsize = 13)
# plt.legend(labels = labels, loc = "upper left") #Dimensions for the legend
# plt.show()

############################################################################################################

# #4 - Making Line Charts
# #commonly used to depict time deries data
#when we have multiple catergories

# df_stocks = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/line_chart_data.csv")
# print(df_stocks)

# #now fixing the date columns, as Python can't read it
# df_stocks["New_Date"] = pd.to_datetime(df_stocks["Date"])
# print(df_stocks["New_Date"]) #Successfully converted Data

# #Also because this data is very long, chart is messy. So we will cut down the data to last 2 quarters of the 2008.
# df_stocks1=df_stocks[(df_stocks.New_Date >= '2008-07-01') &
#                      (df_stocks.New_Date <= '2008-12-31')]
# print(df_stocks1)

# labels2 = ["S&P 500", "FTSE 100"]
# plt.figure(figsize=(20,8))

# plt.plot(df_stocks1["New_Date"], df_stocks1["GSPC500"], color = 'midnightblue')
# plt.plot(df_stocks1["New_Date"], df_stocks1["FTSE100"], color = 'crimson')
# plt.title("S&P Vs FTSE Returns (2008 Q2)", fontsize=14, fontweight = "bold")
# plt.ylabel("Return")
# plt.xlabel("Date")
# plt.legend(labels = labels2, fontsize="x-large")
# plt.show()

########################################################################################################################

#5 - Making Histograms

# # Used represent intervals
# you need to choose number of bins smartly to show your data.
#Use it when there is uniform interval sizes

# sns.set_style("white")

# df_realestate = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/histogram_data.csv")
# print(df_realestate)

# plt.figure(figsize=(8,6))

# plt.hist(df_realestate['Price'], bins = 8, color = "#108A99" )
# plt.title(fontsize=14, fontweight = "bold")
# plt.xlabel("Price in (000'$)")
# plt.ylabel("Number of Properties")
# plt.despine()
# plt.show()

########################################################################################################################

#6 - Making Scatter Plot

#relationship between 2 numeric cordinates
#Help to find data which is far away from maindata & might be incorrect.
#We use this if 2 data has some relation like (money & area size) in buying house

# df_ghar = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/scatter_data.csv")
# print(df_ghar)

# plt.figure(figsize=(12,8))
# scatter = plt.scatter(df_ghar['Area (ft.)'], #scatter is stored for legend, it points to this. to auto copy column names.
#                       df_ghar['Price'],
#                       alpha = 0.6, #to many points overlap, so alpha helps to play with transparency
#                       c = df_ghar['Building Type'], #color will be based on this column
#                       cmap = 'viridis') #this is to choose color
# plt.legend(*scatter.legend_elements(),
#            loc = "upper left",
#            title = "Building Type")
# plt.title("Relationship between Area & Price",
#           fontsize = 14,
#           weight = "bold")
# plt.xlabel("Area (sq. ft.)", weight = "bold")
# plt.ylabel("Price (000's of $)")
# plt.show()

#We can also do plot inside plot using subplot, Learn it when necessary. Below is demo format
#fig, ax = plt.subplot()
#mean.plot.bar(ax=ax, yerr=std,color='lightgreen')

#6(1) - Now Seaborn gives more clearn Scatter Plot, So now we will try it using Seaborn Library

# plt.figure(figsize=(12, 8))
# sns.scatterplot(x=df_ghar['Price'], #Here we have to mention what is x & y axis.
#                 y=df_ghar['Area (ft.)'],
#                 hue=df_ghar['Building Type'],
#                 palette=['black', 'darkblue', 'purple', 'pink', 'white'],
#                 s=100)  # helps adjust intensity & size of dots
# plt.title("Relationship between Area & Price",
#           fontsize=14,
#           weight="bold")
# plt.xlabel("Area (sq. ft.)", weight="bold")
# plt.ylabel("Price (000's of $)")
# plt.show()

#########################################################################################################

#7 - Regression Plot
# Used to get relationship between X-Y
#this was example of linear regression & it may not fit every care specially if data has sudden increase or decrease by huge margin.


# df_ad  = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/scatter_plot_ii.csv")
# print(df_ad)

# sns.set(rc = {'figure.figsize':(9,6)}) #this is same same plt.figure above
# sns.regplot(x="Budget", y="Sales",
#             data = df_ad, #CSV name where data comes
#             scatter_kws= {'color':'k'}, #gives color of dots
#             line_kws= {'color': 'red'}) #gives color of line
# plt.title("Regression Plot",
#           fontsize=14,
#           weight="bold")
# plt.xlabel("X-AXIS", weight="bold")
# plt.ylabel("Y-AXIS", weight="bold")
# plt.show()

######################################################################################################################

#8 - Bar & Line Chart

from matplotlib.ticker import PercentFormatter
df_nuggets = pd.read_csv("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/bar_line_chart_data.csv")
print(df_nuggets)

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)
ax.bar(df_nuggets["Year"],
       df_nuggets["Participants"],
       color = "k")

#Naming the 1 Y-axis
ax.set_ylabel("Number of Participants",
              weight = "bold")
ax.tick_params(axis = "y",
               width = 2,
               labelsize = "large")

ax1 = ax.twinx() #this function helps to merge 2 plots
ax1.set_ylim(0,1) #This it done to add % to left Y-axis
ax1.yaxis.set_major_formatter(PercentFormatter(xmax = 1.0)) #auto imported from matplotlib library

ax1.plot(df_nuggets["Year"],
         df_nuggets["Python Users"],
         color = "#b60000",
         marker = "D") #market of diamond shape

#Naming the 2nd Y-axis
ax.set_ylabel("Python Users",
              color = "#b60000",
              weight = "bold")
ax.tick_params(axis = "y",
               color = "#b60000",
               width = 2,
               labelsize = "large")

#Adding the Final title
plt.title("KD Nuggets Survey of Users", fontsize=14, weight="bold")
plt.show()

