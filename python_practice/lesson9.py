#dictionary
#dictionary is a collection of key-value pairs
#dictionary is unordered, changeable and indexed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

newDict = dict()
newDict["brand"] = "Ford"
newDict["model"] = "Mustang"
newDict["year"] = 1964
print(newDict)

#use dict() constructor to create a dictionary
dict1 = dict(brand="Ford", model="Mustang", year=1964)
print(dict1)

#change value
thisdict["year"] = 2020
print(thisdict)

#add item
thisdict["color"] = "red"
print(thisdict)

#remove item
thisdict.pop("model") #removes the item with the specified key
print(thisdict)

thisdict.popitem() #removes the last inserted item
print(thisdict)

#loop through dictionary
for x in thisdict:
    print(x) #prints the keys

for x in thisdict:
    print(thisdict[x]) #prints the values

for x in thisdict.values():
    print(x) #prints the values

for x in thisdict.keys():
    print(x) #prints the keys

for x, y in thisdict.items():
    print(x, y) #prints the key and value

#copy dictionary
dict2 = thisdict.copy() #returns a copy of the dictionary
print(dict2)
dict3 = dict(thisdict) #returns a copy of the dictionary
print(dict3)

#nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#access nested dictionary
print(myfamily["child1"]["name"]) #prints the name of child1

#loop through nested dictionary
for x in myfamily:
    print(x) #prints the keys of the outer dictionary   

for x in myfamily:
    print(myfamily[x]) #prints the values of the outer dictionary

#loop through all nested dictionary
for x in myfamily:
    for y in myfamily[x]:
        print(y) #prints the keys of the inner dictionary
        print(myfamily[x][y]) #prints the values of the inner dictionary

#loop through all nested dictionary using items()
for x, y in myfamily.items():
    print(x) #prints the keys of the outer dictionary
    print(y) #prints the values of the outer dictionary
    for a, b in y.items():
        print(a) #prints the keys of the inner dictionary
        print(b) #prints the values of the inner dictionary

for x, y in myfamily.items():
    print(x) #prints the keys of the outer dictionary
    for a in y:
        print(a) #prints the keys of the inner dictionary
        print(y[a]) #prints the values of the inner dictionary

#join dictionary
dictA = {"a": 1, "b": 2}
dictB = {"c": 3, "d": 4}
dictC = {**dictA, **dictB} #join dictA and dictB