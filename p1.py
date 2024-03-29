#Typecasting in Python
'''
a = "5"
b =  int(a)
print(type(a))
print(type(b))

'''
'''str1 = "Ashutosh"
abc = str1[:0]
print(str1[::-1])
'''
#Strings are immutable in python
#LIST
#list is a datatype in python which can hold multiple data types.
#It's like an array or tuple but mutable.
"""l1 = [1,2,3,4,5,6,7,8,9,10]
print(l1)
l1.remove(5)
print(l1)
"""
#Tuples
#Tuples are immutable just like strings.
#Tuples are used to store multiple items in a single variable.
"""tup = (1,2,3,"ashu",True)
print(tup)"""
#Sets
#sets are used to store unique values in a single variable.
#sets are unordered and unindexed.
#sets are mutable in nature that is we can add and remove elements from it.
# examples 
"""s1 = {1,2,3,4,5,6,7,8,9,10}
print(s1)"""
# we can also use some methods in sets like add, remove, discard, pop, clear, union, intersection, difference
"""s1.add(11)
print(s1)"""
#we can make an empty set using set() function
"""b = set()
print(type(b))"""

#Dictionary
#Dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets, and they have keys and values.
#example
"""d1 = {
    "name":"Ashutosh",
     "age" : 20,
    "address" : "Delhi"
}

print(d1.get("lock")) #returns none if key is not present
print(d1["name"])   #accessing the value of name key if key not present it will give error.
print(d1)
print(d1.keys()) #this will return all the keys of dictionary
print(d1["name"]) # this will give value of name key
print(d1.values()) # this will return all the values of dictionary
# and to show empty dict we can use the following code
d2 = {}"""
"""Age  = int(input("Enter Your age : "))
if(Age>18):
    print("You are eligible to vote")
elif(Age>10 and Age<18 ):  
    print("Your are still child")
else:
    print("you are too young to vote ")"""
    
#Match case in python (new addition in python 3.10)

"""a =2
match a:
    case 1:
        print("one")
    case 2:
        print("two")
    case 3:
        print("three")
    case _:
        print("default")"""
        
#similar to switch case in c++ and java

#LOOPS
#FOR LOOP
"""for i in range(5):
    print(i+1)"""
#to print a list or a tuple
"""l1 = [1,2,3,4,5,6,7,8,9,10]
for item in l1:
    print(item)"""
# to brake loop we use break statement 
"""for item in l1:
    if item == 4:
        break
    print(item)"""
    
#WHILE LOOP
"""num = 2
while (num<10):
    print(num+1)
    num +=1
print("Done with the loop")"""

"""
This is Infinite While loop
while(true):
    print("Waiting for the user to press ctrl+c to stop the loop")
"""
#continute statement skips the execution of remaining code
# inside while loop and goes back to test condition.


#Functions are block of code which is executed when it is called.
#basic function example
"""def Ashu():
    print("Hello ashu")
Ashu()"""
#Functions can take multiple arguments separated by comma.
#example
"""def greet(name,surname):
    print("Hello",name,surname)
    
greet("Ashutosh","Pandey")"""

#concept of f strings in functions
"""def hello(name,surname,date):
    str = f"Hello Mam I'am {name} {surname} and I will not be available on {date}"
    print(str)
hello("Ashutosh","Pandey","20th August")"""

# output -> Hello Mam I'am Ashutosh Pandey and I will not be available on 20th August
#this is similar to template litrals in javascript

#Exception Handling
"""
try:
    a = int(input("Enter a number : "))
    print("hello"+a)

except:
    print("Invalid Input")"""
    
#File Handling/input output
#to write in a file 
#exmple for a string
"""s = "Hello World"
with open ("file.txt","w") as f:
    f.write(s)
print("Data written successfully")

#To read the file
with open("file.txt","r") as f:
    a = f.read()
    print(a)"""
    
#By using with statement we can avoid using close() method.
#because it automatically closes the file after its suite finishes.

#To append in a file
#example
"""a = "\tAshutoh Pandey"
with open("file.txt","a") as f:
    f.write(a)
print("Data appended successfully")"""

#it adds the data at the end of the file.
