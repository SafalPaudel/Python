########  Maniulating Tuples  ###########

#Tuples are immutable, hence if you want to add, remove or change tuple items, 
# then first you must convert the tuple to a list. Then perform operation on that list and convert it 
# back to tuple.


countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)


Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)


Tuple = (0, 1, 2, 3, 2, 32, 1, 3, 2,3)
res = Tuple.index(3,4,8)
print('First occurrence of 3 is', res)

print(len(Tuple))