# name=input('input your name')
# age=int(input('input your age'))
# print(name , age)


# sentences =input('write ur sentence')
# word1=input('word you want to replace ')
# word2=input('word you want to replace with')
# print(sentences.replace(word1 ,word2))
# countries =list(('hello',"there",33))
# print(countries)


# list1 = [1, 2, 3, 6, 4]
# list1.sort()
# print(list1)
#! list is a collection of order elements and it's mutable[]
#! tuple' it like list but immutable , object does not support item assignment ()
#! set is a collection of unique elements and unordered  and immutable {}
# ! dictionary is a collection of key value pairs and unordered and immutable{key:value}

# like below
# when we use three_num=() prentices that's mean it's immutable (we cant change it )
# we will see error as below:
# three_num = (1, 3, 7)
# three_num[2] = 5
# print(three_num[2])
# print(type(three_num))


# /////////////// functions in python
#! in function we must add the indentation so we write below with 4 space or indentation

# def greetings_fun():
#     print("hello")
# greetings_fun()


# def greetings_fun(name):
#     print("hello " , name)


# greetings_fun("hiba")


# !!!!!!!!!!!! if statement in python

# value = int(input("input then we will print your input"))
# if type(value) == str:
#     print(value, "is a string")
# elif type(value) == int:
#     print(value, "is an int")
# else:
#     print(value, " we don't now")
# !  module in if statement
# if value % 5 == 0:
#     print("is module")
# else:
#     print("is not a module by 5")


# ! Dictionary in python
# my_dict = {
#     "name": "Tim",
#     "email": "hello@hello.com",
#     "nationality": "African",
#     "age": 34

# }
# print(my_dict["email"]) to get the value of the email key but if not found wil through an error
# print(my_dict.get("email")) if not found will return None 

# ! while loop
# i = 1
# while i < 6 or i == 6:
#     print(i)
#     i += 2


# ! for loop in python

# list2 = [1, 2, 3, 5, 6, 8]
# for num in list2:
#     print(num)

# letters = "hello"
# for letter in letters:
#     print(letter)


# my_obje = {
#     "name": "hiba", "age": 33
# }
# for obj in my_obje:
#     print(obj)

# # !range
# for num in range(10):
#     print(num)

# for num in range(10, 17):
#     print(num)
# else:
#     print("finish looping")


# ! nested list in python

# nested_list = [[1, 2, 3, 4, 6], [2, 4, 5, 7, 9], [6, 0, 55]]

# for lists in nested_list:
#     for row in lists:
#         print(row)


#!  try except method (just like try catch)
# try:"hello"
# except:"do  some thing"
# finally:"do some thing"
# //2
# try:
#     x = int(input("an integer number"))
#     print(x)
# except:
#     print("wrong input " + name)

# ! reading files/////////////////////////////////

# country_file = open('countries.txt', 'r')
# # print(country_file.readlines())
# for lines in country_file.readlines():
#     print(lines)
# country_file.close()


# count_file = open('countries.txt', 'r')
# print(count_file.readlines())
# for lines in count_file.readlines():
#     print(lines)
# count_file.close()


# ! writing in file
# country_file = open('country.txt', 'w')
# country_file.write("hello there for the country file")
# country_file.close()


# !classes in python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# name = input("inter name")
# p1 = Person(name, 33)
# print(p1.name)
# del p1
# # print(p1)
# p2 = Person(name, 33)
# print(p2)

# ! inherit from other classes
# from new import Student


# class Person(Student):
#     pass    to pass any error


# p1 = Person()
# print(p1.name)

# ! using python shell just search about idle which installed dynamically when install python

# ! simple signup and login system
# ! import modules in python
import new_Module
new_Module.say_hello()
new_Module.call_yourName()
# ? to start anew django app :  django-admin startproject djangoapp
