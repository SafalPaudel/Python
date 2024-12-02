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



l = [1,4,8,5,2,9,13,26,1,11]
print(l)
l.append(7)
l.sort(reverse = True)
l.reverse()
print(l)
print(l.index(4))
print(l.count(1))

m=l.copy()
m[0]=0
print(l)

l.insert(1,56)           # 1 is indes and 56 is the value that is stored in index 1 and other are shifted
print(l)

m = [900, 1000, 1100]
k = l + m
# l.extend(m)
print(k)








