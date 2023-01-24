# def funcName():
#     print("hello")

# funcName()

#######################

# def update(x):
#     print(id(x))
#     x=10
#     print("x ",x)
#     print(id(x))

# y=5
# print(id(y))
# update(y)
# print("y ",y)

##########################

# x=10
# print(id(x))
# x=10
# print(id(x))
# x=10
# print(id(x))

##########################

# def person(name, **data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)

# person("bhanu", age=21, hobby="painting")

############################

a = 10
print(id(a))

def func():
    a=9
    x=globals()['a']
    print(id(x))
    globals()['a'] = 15
    print(id(globals()['a']))
    print("x is ",x)

func()
print(a)
print(id(a))

