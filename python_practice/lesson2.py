a = 5
b = 'Hello! World'
print(b)
print(b[3:6]) #print range
print(b[:5]) #print range from start

c="Hello! World "
print(c.upper())
print(c.lower())
print(c.strip()) #remove whitespace from start to end

print(b + " " + c) #concatenate string

price = 10
name = "orange"
print(name,price) #concatenate int with string by using comma (,)

#using format() or f to concatenate #only in python 3.6 and upper
txt = f"The price of {name} is {price} Ks"
print(txt) #The price of orange is 10 Ks

#using modifier within placeholder
txt2 = f"The price of {name} is {price:.2f} Ks"
print(txt2) #The price of orange is 10.00 Ks
