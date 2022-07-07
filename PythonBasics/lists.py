demo_list = [1, "Hello", 1.34, True, [1,2,3]]
colors = ["red", "green", "blue"]

numbers_list = list((1,2,3,4))

r = list(range(1,10))
print(r)
print(len(demo_list))
print(colors[-2])

print(colors)
colors[1] = "yellow"

# colors.append("violet")
# colors.extend(["violet", "yellow"])
# colors.insert(1,"violet")
# colors.remove("green")

# print(colors)

# colors.pop(1) #Removes one element, if argument is not given it removes last element

# colors.sort()
# colors.sort(reverse=True)
# print(colors)

print(colors.index("yellow"))
print(colors.count("red"))
