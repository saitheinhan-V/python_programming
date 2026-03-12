thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print(thistuple[-1]) #refere to last item
print(thistuple[-2]) #refere to 2nd last item
print(thistuple[0:2]) #from index 0 to index 2 (not included)
print(thistuple[2:]) #from index 2 to the end
print(thistuple[:2]) #from the beginning to index 2 (not included)

#update tuple
x = ("apple", "banana", "cherry")   
y = list(x) #convert tuple to list
y[1] = "kiwi" #update the list
x = tuple(y) #convert list back to tuple
print(x)

#unpack tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green) #apple
print(yellow) #banana
print(red) #cherry


#join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple2 * 2 #repeat the items in tuple2 twice
print(tuple4)

tuple5 = tuple1 * 3 #repeat the items in tuple1 three times
print(tuple5)