import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stat
import pylab

# Define our dataset
dataset = [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

#plt.hist(dataset)
#plt.show()

# Z-Score Method
outliers=[]
def detect_outliers(data):
    threshhold = 3 #3rd Standard Deviation
    mean = np.mean(data)
    std=np.std(data)

    for i in data:
        Z_score = (i-mean)/std
        if np.abs(Z_score)>threshhold:
            outliers.append(i)
    return outliers

print(detect_outliers(dataset))

#IQR Method
#1. Sort the data
#2. Calcualte Q1(25%) & Q3(75%)
#3. IQR (Q3-Q1)
#4. Find the lower Fence(Q1-1.5(iqr))
#5. Find the Upper Fence(Q3+1.5(iqr))

q1, q3 = np.percentile(dataset, [25,75])
print(q1,q3)

iqr = q3 - q1
print(iqr)

#find the lower fence & Upper fence
lower_fence = q1-(1.5*iqr)
upper_fence = q3+(1.5*iqr)
print(lower_fence, upper_fence)

#sns.boxplot(dataset)
#plt.show()

#sns.histplot(dataset,kde=True)
#plt.show()

#Normal Distribution data
s = np.random.normal(0.5,0.2,1000)
sns.histplot(s,kde=True)
#plt.show()

mu, sigma = 3., 1. #mean & std 
H = np.random.lognormal(mu,sigma,100)
sns.histplot(H,kde=True)
#plt.show()

sns.histplot(np.log(H), kde=True)

#If you want to check if feature is guassian or normal Distributed
# Q-Q plot
def plot_data(sample):
    plt.figure(figsize=(10,6))
    plt.subplot(1,2,1)
    sns.histplot (sample)
    plt.subplot(1,2,2)
    stat.probplot(sample, dist='norm', plot=pylab)
    plt.show()

s = np.random.normal(0.5,0.2,1000)
plot_data(s)