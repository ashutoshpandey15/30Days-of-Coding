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

#Dictionary
#Dictionary is a collection which is unordered, changeable and indexed.
#In Python dictionaries are written with curly brackets, and they have keys and values.
#example
d1 = {
    "name":"Ashutosh",
     "age" : 20,
    "address" : "Delhi"
}
print(d1)
print(d1.keys()) #this will return all the keys of dictionary
print(d1["name"]) # this will give value of name key
print(d1.values()) # this will return all the values of dictionary