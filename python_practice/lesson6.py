thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist.append("orange")
print(thislist)

thislist.remove("kiwi")
print(thislist)

thislist.pop(1)
print(thislist)

thislist.pop() #removes the last item
print(thislist)

del thislist[0] #removes the first item
print(thislist)

#del thislist #deletes the entire list

thislist.clear() #empties the list
print(thislist)

list1 = ["a", "b", "c"]
for x in list1:
    print(x)

list2 = ["d", "e", "f"]
print(len(list2))
for i in range(len(list2)):
    print(list2[i])

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#newList = [x for x in fruits if "a" in x]
newList = [x if x != 'apple' else 'orange' for x in fruits ]
print(newList)

#sort
number = [1, 5, 3, 4, 2]
number.sort()
print(number)

number.sort(reverse=True)
print(number)

#sort with custom function
def myfunc(n):
  return abs(n - 50)#sort based on the distance from 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#case sensitive sort
fruits.sort(key = str.lower)
print(fruits)

#copy list
mylist = fruits.copy()
print(mylist)

mylist2 = list(fruits)
print(mylist2)

mylist3 = fruits[:]
print(mylist3)

#join list
list1 = ["a", "b", "c"]
list2 = ["d", "e", "f"]
list3 = list1 + list2
print(list3)

#append list
for x in list2:
    list1.append(x)
print(list1)

#extend list
list1.extend(list2)#adds list2 at the end of list1
print(list1)

