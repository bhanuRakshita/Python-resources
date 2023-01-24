from numpy import *

# #Adding two arrays
# arr1 = array([10,20,30])
# arr2 = array([50,60,70])

# arr3 = arr1+arr2
# print(arr3)

#copying an array
# arr1=array([[2,5,3,3,2,6],[7,2,8,4,3,6]])
# arr2=arr1; #same address
# arr3=arr1.view() #shallow copy
# arr4=arr1.copy() #deep copy
# arr5=arr1.flatten()
# arr6 =arr5.reshape(2,6)
# print(arr6)

#matrices
arr1=array([
            [22,55,33,36],
            [72,23,82,43],
            [30,16,32,23],
            [45,13,52,45],
            ])
m = matrix(arr1);
print(diagonal(m))
m1 = matrix('1 2 3; 4 5 6; 7 8 9')
m2 = matrix('5 3 1; 4 5 6; 7 2 0')
# print(m1*m2)
