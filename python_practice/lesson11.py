i = 0
num = [5,8,9,12,4,3,6,7,2,1]
divisor = 2
while i < num.__len__():
    if(num[i] % divisor == 0):
        print(f"{num[i]} is divisible by {divisor} with the index of {i}") #prints the value of i when it is divisible by 10
        break
    i += 1
else:
    print("nothing found") #prints when the condition is false