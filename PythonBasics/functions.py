#Funtion definition
def hello(name="Person"):
    print("Hello " + name)

hello("Daniel")
hello()

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10,30))

#Lambda definition
add = lambda numberOne, numberTwo: numberOne + numberTwo

print(add(1,5))