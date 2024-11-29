#################       LIST      ############################

marks =[3,4,5, "Safal", False]
print(type(marks))
print(marks)

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])


colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])



colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:             # in keyword used to find value present in list colors
    print("Yellow is present.")
else:
    print("Yellow is absent.")


if "Red" in colors:
    print("yes")

# Same thing applies for integer and strings


print(colors[1:])
print(colors[1:4])
print(colors[1:2:3])



animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])


names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)