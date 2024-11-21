
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!= 80:
        print(x, "is not 80")
    case _:
        print(x)




name = 'Safal'
for i in name:        # prints every single character
    print(i)
    if(i=="a"):
        print("This is something special")


colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
    for i in x:          
        print(i)


for k in range(5):
    print(k)      #doesnt include 5
    

for k in range(1,20000):
    print(k+1)       # it includes 20000


for k in range(2,12,4):
    print(k)         # 2,6,10

for k in range(1,12,3):
    print(k)      # 1,4,7,10



i= int(input("Enter the number :"))
print(i)
while(i<=38):
    i = int(input("Enter the number :"))    
    print(i)
  

print("Done with the loop")

count = 5
while (count > 0):
  print(count)
  count = count - 1
else:
  print("I am inside else")


while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0:
    break