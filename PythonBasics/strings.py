myStr = "hello world"

print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace('hello', 'bye'))
print(myStr.count(' '))

print(myStr.startswith('he'))
print(myStr.endswith('world'))

print(myStr.split('o'))
print(myStr.find('z'))

print(len(myStr))
print(myStr.index('e'))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])
print(myStr[-1])
print(myStr[-5])

my_name = 'Daniel'
print("My Name is " + my_name)
print(f"My name is {my_name}")
print("My name is {}".format(my_name))
