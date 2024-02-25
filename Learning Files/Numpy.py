import numpy as np 

v = [1, 2, 3]
v_np = np.array([1,2,3])
print(v), print(v_np)

#Vectors
print("\nVectors")
m = np.array([5,12,6])
print(m)

#Matrices
print("\nMatrices")
m = np.array([[5,12,6],[-3,0,14]])
print(m.shape) #Output: 2,3
print(m)

#Creating A Tensor
print("\nTensor")
m1 = np.array([[5,12,6],[-3,0,14]])
m2 = np.array([[9,8,7],[1,3,-5]])
t=np.array([m1,m2])
print(t)

#Addition of Matrices (Dimension should Be Same)
print("\nAddition of Matrices")
print(m1+m2)

#Transpose of Matrices - Means flipping rows & columns
print("\nTranspose of Matrices")
a = np.array([[5,12,6],[-3,0,14]])
print(a.T) #.T attribute is used to obtain the transpose of a NumPy array.

#Scaler Product of Vectors
print("\nScaler Product")
x = np.array([2, 8, -4])
y = np.array([1, -7, 3])
print(np.dot(x,y))

#Numpy Fundamentals
print("\nNumpy Fundamentals")
array_a = np.array([[1,2,3],[4,5,6]])
print(array_a[0])
print(array_a[0][1])
print("\nLine 45\n",array_a[1,1])
print("\nLine 46\n",array_a[:,0])
print("\nline 47\n",array_a[-1])

print("\nline Break\n")
array_a[0, 2] = 9
print(array_a)
array_a[:,0] = 9
print(array_a)
array_a[:] = 9
print(array_a)

print("\nline Break\n")
array_b= np.array([7,8,9])
array_b += 2
print(array_b)
print()
print(array_a)
print("\nLine 63\n",array_a * array_b)

#Type Casting
print("\n Type Casting")
array_c= np.array([[4,1,3], [4,5,6]])
array_d= np.array([2,6,11]) 
print(type(array_d)) #ND Array
print(np.add(array_c, array_d, dtype = np.float64))

print(np.mean(array_c, axis=0))

#reading CSV
print("\nReading CSV")
RB = np.genfromtxt('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Numpy.csv', delimiter = ',')
print(RB)

RB = np.genfromtxt('C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Numpy.csv', delimiter = ',', skip_footer=1, skip_header=2)
print(RB)

# Saving your data with Numpy Npsave
print("\nNPsave")
lending_co = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-Company-Saving.csv", delimiter=',', dtype=str)
print(lending_co)

#saving the CSV as npy file & loading it - Npy files are very fast
np.save("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-Company-Saving", lending_co) #The first argument specifies the filename without the extension, and the second argument is the array to be saved.
lending_loadnpy = np.load("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-Company-Saving.npy")
print(lending_loadnpy)
print("\nLine 91\n",np.array_equal(lending_loadnpy, lending_co))

#saving the CSV as npz file with np.savez & loading it - Npz files are very fast
print("\nNpSavez")
np.savez("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-Company-Saving", lending_co, jadu = lending_loadnpy) #loaded from code @89
lending_loadnpz = np.load("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/Lending-Company-Saving.npz")
print(lending_loadnpz["arr_0"]) #(Automatically lending_co is stored as arr_0)arr_0 will print value from lending_co & arr_1 will print values from lending_loadnpy
print("\nLine 98\n",lending_loadnpz["jadu"]) #(This calls second arguments) We can store any amount of array in Npz format so we can call multiple files saved in it using arguments

#numpy can only read numeric values - So we use Dtype to show values
print("\nString & numbers")
lending_co_lt = np.genfromtxt("C:/Users/jayan/OneDrive/Documents/Data Analytics/Data Sets/lending-co-LT.csv", delimiter=',', dtype = str)
print(lending_co_lt)

#working with Arrays & Slicing
print("\nArray & Slicing")
matrix_b = np.array([[1,1,1,3,0], [3,5,3,2,3], [4,5,5,6,7]])
print("\n",matrix_b[:,:])
print("\n",matrix_b[::2,::])
print("\n",matrix_b[::,::2])
print("\n",matrix_b[::2,::2])

print("\n",matrix_b[:,0])
print("\n",matrix_b[:,0]> 2) 

print("\n",matrix_b[matrix_b[:,:] % 2 == 0]) 
print("\n",matrix_b[(matrix_b[:,:] % 2 == 0) & (matrix_b[:,:] == 4 )]) # And Conditions
print("\n",matrix_b[(matrix_b[:,:] % 3 == 0) | (matrix_b[:,:] == 6 )]) # Or Condition

