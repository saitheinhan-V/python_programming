def myFunction(name):
    print("Hello",name)

myFunction("Alice")

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

def mySum(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum
print(mySum(1, 2, 3))
print(mySum(4, 5, 6, 7))