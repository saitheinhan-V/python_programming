x = 5
y = 8

z = y * x
print(z)

z = y / x
print(z)

z = y // x
print(z)

z = y ** x
print(z)

x >>= 3
print(x)

z = x ^ y
print(z)

z = 5 >> 2
print(z)

"""
x=3
print(x)
"""
print(x:=3) 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #true
print(x is y) #false
print(x == y) #true
print(x is not y) #true
print(x is not z) #false

#membership 
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits) #true
print("guava" not in fruits) #true
print("cherry" not in fruits) #false