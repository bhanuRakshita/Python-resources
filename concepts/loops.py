# return found if there's even one num div by 5 or else not found

# for i in [4,23,46,40,43]:
#     if i%5==0:
#         print("found")
#         break
# else:
#     print("not found")

###############################

#find a prime number

# num = int(input("Pls enter a number: "))
# if(num!=1):
#     for i in range(2,num):
#         if num%i==0:
#             print("not a prime number")
#             break
#     else:
#         print("It's a prime num!!!")

# else:
#     print("DUDE! 1 is not a prime number")

########################################

# prompt user to enter an array

from array import *

arr = array('i',[])
len = int(input("Enter a length: "))
for i in range(0,len):
    x = int(input("input value: "))
    arr.append(x)
for i in arr:
    print(i, end=" ")
