# for i in range(4):
#     for i in range(4):
#         print("#",end="\t")
#     print("\n")

# max=4
# for i in range(max):
#     for j in range(i+1):
#         print("#",end="\t")
#     print("\n")

max=4
for i in range(max):
    for j in range(max-i):
        print("#",end="\t")
    print("\n")

max=4
counter=1
for i in range(max):
    for j in range(i+1):
        print(counter,end="\t")
        counter+=1
    print("\n")


   