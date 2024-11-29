# def average(a,b):
#     print("The average is" , (a+b)/2)

# average(4,5)


# def name(fname, mname = "Prasad", lname = "Paudel"):
#     print("Hello,", fname, mname, lname)

# name("Safal")

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill","Paudel")


# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum= sum + i
#     print("Average is:", sum / len(numbers))
    
# average(5,6,4,5,6,3,2)


################  DICTIONARY CLASS #############

# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")



def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum= sum + i
    #print("Average is:", sum / len(numbers))
    return 9             # here first return only runs ...other second third return will not run
    return sum / len(numbers)
c=average(5,6,4,5,6,3,2)
print(c)

