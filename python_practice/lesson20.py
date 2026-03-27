cars = ["Alphard","Toyota","Honda","Nissan"]
for car in cars:
    print(car)

cars.pop(1)
print(cars)

#iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

myStr = "apple"
myit = iter(myStr)
print(next(myit))
print(next(myit))