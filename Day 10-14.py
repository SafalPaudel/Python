name  = "SAFAL"

print("Hello,"+ name)

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#print(name[5]) Throws error

name = "Apple"
print("Lets use a for Loop\n")
for character in name:
    print(character)



name = "Safal,Pro"
print(name[0:5])  #5 = n-1
len1=len(name)
print("I am a",len1, "Don")


fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4])   # including 0 but not 4
print(fruit[:4])  # 0 is automatically kept by python
print(fruit[1:4])  # including 1 but not 4
print(fruit[:])
print(fruit[0:-3])
print(fruit[0:len(fruit)-5])
print(fruit[-3:-1])


#Quick Quiz

nm = "Safal"
print(nm[-4:-2])    # ans = 5-4= 1   and 5-2=3 so [1,3] here 1 is included but not 3 

#Strings are immutable
a= "Safal"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.lower()+a.upper())


a="!!!Safal !!!!!!! Safal"
print(a.rstrip("!"))       # removes !!!!!!!!! of behind not front
print(a.replace("Safal","SAFAL"))  # replaces all safal with SAFAL
print(a.split(" "))  # splits the a where there are spaces into list


Heading = "introduction tO pythoN"
print(Heading.capitalize())   # first word ie. i is made capital I ans also makes all the remaining words small

str1= "Welcome to my Github !!!"
print(str1.endswith("!!!"))    # True or false and it is true

str1= "Welcome to my Github !!!"
print(str1.endswith("to", 4,10))    # True or false and it is true

str1 = "He's name is Dan. He is an honest man."
print(str1.find("isa"))    # if the word is preset then we will get True but if not then we will see -1
print(str1.index("is"))    # gives the index value of that wird ie.is giving value of i only

str1 = "WelcomeToTheConsole1"
print(str1.isalnum())     # returns True only if the entire string only consists of A-Z, a-z, 0-9 no spaces or other punctuations

str1 = "Welcome"
print(str1.isalpha())   # it must contain strings only like a-z or A-Z and not spaces

str1= "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas"   # \n is not sprintable so it will be false if used
print(str1.isprintable())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"    # small will be big and big will be small
print(str1.swapcase())


a= int(input("Enter your age:"))
print("Your age is:",a)
# Conditional Operators
# > , < , >= , <= , ==
# print(a>18)
# print(a==18)
# print(a<=18)
# print(a!=18)
if(a>18):
    print("you can drive")
    print("Yes")
else:
    print("you can't drive")
    print("no")
    print("Sorry")


applePrice = 190
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")


num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")




num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")



