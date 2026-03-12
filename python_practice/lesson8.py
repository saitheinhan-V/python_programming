#set
fruits = {"apple", "banana", "orange"}
print(fruits)

fruits.add("kiwi")
print(fruits)

fruits.update(["grape", "melon"])
print(fruits)

fruits.remove("banana")
print(fruits)
fruits.discard("grape")#removes the specified item, if it exists. If the item does not exist, do nothing
print(fruits)
fruits.pop() #removes a random item
print(fruits)
fruits.clear() #empties the set
print(fruits)

#join set
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #join set1 and set2
print(set3)

set4 = set1 | set2 #join set1 and set2
print(set4)

set5 = set1.intersection(set2) #returns the items that are present in both sets
print(set5)

set6 = set1 & set2 #returns the items that are present in both sets
print(set6)

set7 = set1.symmetric_difference(set2) #returns the items that are present in either set1 or set2, but not in both
print(set7)

set8 = set1 ^ set2 #returns the items that are present in either set1 or set2, but not in both
print(set8)

set9 = set1.difference(set2) #returns the items that are present in set1 but not in set2
print(set9)

set10 = set1 - set2 #returns the items that are present in set1 but not in set2
print(set10)

set11 = set1.issubset(set2) #returns True if all items in set1 are present in set2
print(set11)

set12 = set1.issuperset(set2) #returns True if all items in set2 are present in set1
print(set12)

set13 = set1.isdisjoint(set2) #returns True if no items in set1 are present in set2
print(set13)

set14 = set1.copy() #returns a copy of set1
print(set14)

set15 = set(set1) #returns a copy of set1
print(set15)

set16 = set1.clear() #empties the set
print(set16)

set17 = set1.pop() #removes a random item from the set and returns it
print(set17)

s
