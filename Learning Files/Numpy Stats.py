import numpy as np
list(range(1,10))

array_rng = np.arange(30)
array_rng = np.arange(start = 0, stop = 30, step = 2)
print(array_rng)

#used to get Random function
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg

array_RG = gen(pcg())
print(array_RG.normal(size = (5,5))) #The normal function generates random numbers

print("\n Line 15 Starts\n")
array_RG = gen(pcg(seed=365))
print(array_RG.integers(low = 10, high = 100, size = (5,5))) #The integers function generates random integers between the low and high values
print(array_RG.poisson(lam = 10, size = (5,5)))
print(array_RG.binomial(n=100, p = 0.4, size = (5,5)))
print(array_RG.logistic(loc = 9, size = (5,5)))#Average of rows will be 9

#Use this link to know more about these random function & their practical usage
#https://chat.openai.com/share/8ca10f82-1346-4bfa-bf8a-89ef128bb376

#Statistics In Numpy Python
print("\n Statistics\n")
matrix_A = np.array([[1,0,0,3,1],[3,6,6,2,9],[4,5,3,8,0]])
print("\n",matrix_A)

print("\n",np.mean(matrix_A))
print("\n",np.mean(matrix_A[0]))
print("\n",np.mean(matrix_A, axis=0)) #axis 0 is mean of 1,3,4
print("\n",np.mean(matrix_A, axis=1)) #axis 0 is mean of 1,0,0,3,1

print("Line 36\n",np.min(matrix_A))
print("Line 37\n",np.min(matrix_A, axis=0)) #it takes minimum from each row
print("Line 38\n",np.minimum(matrix_A[0], matrix_A[2])) #Minimum of 2 element in array_a = [][][]

print("Line 40\n",np.ptp(matrix_A)) # returns the difference between highest & lowest values in an array
print("Line 41\n",np.ptp(matrix_A, axis=0)) #will compare element columnwise

print("Line 43\n",np.sort(matrix_A, axis = None))
print("Line 44\n",np.percentile(matrix_A, 70)) #70th percentile is greater than 70% of the data - The 70th percentile is the value below which 70% of the data falls.
print("Line 45\n",np.percentile(matrix_A, 70, method = 'lower')) #lower can be replaced with - Higher, nearest, midpoint
print("Line 46\n",np.quantile(matrix_A, 0.70, method = 'nearest'))

#mean - Average Value (8,9,8,8)/4=$$
#mode - Value repeated maximumm times
#median - Mid value - Divide if even numbers

print("Line 48\n",np.median(matrix_A))
print("Line 49\n",np.average(matrix_A)) #This is mean
print("Line 50\n",np.var(matrix_A)) #variance measures how much the values in the dataset deviate from the mean
print("Line 51\n",np.std(matrix_A)) #standard deviation is the square root of the variance
 
#cov is a symmetric matrix
print(np.cov(matrix_A)) #First line shows covarience of that line with other & so on..

#Histograms
print("\nHistograms")
matrix_A = np.array([[1,0,8,4,1],[3,7,6,1,9],[4,5,1,8,0]])
np.sort(matrix_A)
print("\n",np.histogram(matrix_A))
print("\nLine 65",np.histogram(matrix_A)[0]) #only gives first array outpit

hist, bins = np.histogram(matrix_A, bins = 4)
print("\n", hist, bins) # "bins" refers to the number of intervals or divisions used to group and count the values in the histogram.

#Visualtion starts Here
np.sort(matrix_A)

import matplotlib.pyplot as plt
sorted_bins = np.sort(bins)
plt.hist(matrix_A.flat, bins= sorted_bins)
plt.show()

matrix_AB = np.array([[1,0,8,4,1],[3,7,6,1,9],[4,5,1,8,0]])
print(np.histogram2d(matrix_AB[0], matrix_AB[1], bins = 4))

#Sampling Types
#1 Simple random sampling - Randomly people are selected & questions are asked.
#2 Stratified Sampling - When surveys are done on 2 groups where they aren't overlapping.
#3 Systematic Sampling - Chosing people after every fixed interval - 4th Interval
#4 Convenience Sampling - Choosing domain experts for survey, Kidney survey only by doctors.

#Varible - which take value input & it also means 'changing' - Varible petrol price

