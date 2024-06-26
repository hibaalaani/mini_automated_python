#TASK 9- BONUS TASK

import calendar
import sys
# exercise from basic python
# num1 = input('Enter a number1: ')
# num2 = input('Enter a number2: ')

# num3 = input('Enter a number3: ')
# sum = int(num1) +int(num2)  +int(num3) 
# triple = sum*3
# bool1 = bool(num1 == num2 == num3)
# if (bool1):
#     print(triple)
# else:
#     print(sum)    

""" print('Print a calendar for a year and month:')
month = int(input('Month (mm): '))
year = int(input('Year (yyyy): '))
print('\n')

calendar.setfirstweekday(calendar.SUNDAY)
cal = calendar.monthcalendar(year, month)

if len(str(month)) == 1:
    month = '0%s' % month

# Header
print('|++++++ %s-%s +++++|' .format(month, year))
print('|Su Mo Tu We Th Fr Sa|')
print('|--------------------|')

# display calendar
border = '|'
for week in cal:
    line = border

    for day in week:
        if day == 0:
          # 3 spaces for blank days
            line += '   '
        elif len(str(day)) == 1:
            line += ' %d ' % day
        else:
            line += '%d ' % day
    # remove space in last column
    line = line[0:len(line) - 1]
    line += border
    print(line)

print('|--------------------|\n') """


# TASK 6
# input_1 = input("Type F for Farenheit and C for Celsius: ")
# input_2 = float(input("Type the value to convert: "))
# if input_1 == "C":
#     F = (input_2*9/5)+32 # formula
#     print("The value in Farenheit is ", F)
# else:
#     C = (input_2-32)*5/9 # formula
#     print("The value in Celsius is ", C)


# task 7 
# first way
# a, b = 0, 1
# c=0
# print(a, b)
# while c<50:
#     print(c)
#     c = a + b
#     a = b
#     b = c

# second way
#Task 8
# def fibonacci_series():
#     num1, num2 = 0, 1
#     while num1 < 50:
#         print(num1, end=" ")
#         num1, num2 = num2, num1 + num2 #swap the values
# fibonacci_series()
# import datetime
# from dateutil import tz
# import time
# print(time.time())
# print(datetime.datetime.now() - datetime.datetime(2020, 1, 1))

# print(tz.gettz('Europe/London'))
# import os

# print(os.path.isfile('/home'))


# import dbm
# db = dbm.open('test22' , 'c')

# db['hello']= 'kill the messenger'
# db['2024']= 'Interstellar'

# print(db['hello'])

# for item in db:
#     print(item , db[item])
    
# import pickle
# s = pickle.dumps([1,5,7])
# opj = pickle.loads(s)
# print(opj)    

import datetime
import calendar





def get_birthday(str):
    birthday = datetime.datetime.strptime(str, '%Y-%m-%d')
    this_year = datetime.datetime.now().year
    print(birthday , this_year)
    
    return datetime.datetime(this_year , birthday.month , birthday.day)


print(get_birthday('1987-12-14'))




def get_weekday(str):
   bd = get_birthday(str)
   date = bd.weekday()
   day_name = calendar.day_name[date]
   print(day_name)
   
   
get_weekday('1987-12-14')   



def get_num_day(date_str):
    # list_value = date_str.split('-')
    
    # year = int(list_value[0])
    # month = int(list_value[1])
    # day = int(list_value[2]) 
    
    # date_obj = datetime.date(year, month, day)
    bd =get_birthday(date_str) 
    num_day =(bd- datetime.datetime(bd.year , 1 ,1 )).days
    print(num_day+1)
get_num_day('1987-2-14')    




def defference_number(str1 , str2):
    
   diff = ( datetime.datetime.strptime(str1, '%Y-%m-%d')-datetime.datetime.strptime(str2, '%Y-%m-%d')).days
   print(diff)
   
defference_number('1987-12-14', '1987-10-16')   
   
   


def num_of_days(str):   
    bd =datetime.datetime.strptime(str, '%Y-%m-%d')
    test =  bd.isocalendar()
    days_num =( datetime.datetime.now()-bd).days
    print(calendar.month(bd.year,bd.month))
    # to get num of sunday days
    # sun = 6
    # count =0 
    # for i in range(days_num+1):
    #     print()
    #     check_day = bd +datetime.timedelta(days=i)
    #     if check_day.weekday() == sun:
    #         count += 1
    #         print(count)     
    print(test , days_num)
num_of_days('1987-12-14')






# import datetime

# def test (d1, d2):
#     dt = datetime.datetime.strptime(d1,d2)
#     wt = dt.strftime('%W') # to get the week number based on Sunday """
#     week_num = dt.isocalendar()[1] # to get the week number assuming Monday is start the week"""
#     w_name = dt.strftime('%A')
 
#     return wt ,week_num,w_name


# print(test('1987,1,21', '%Y,%m,%d'))



#! List Comprehension

nums = [ 1, 2,3 ,4 ,5, 6,7, 8]
print([num for num in nums if num%2 != 0 ])
print([num * 2 if num % 2==0 else num/2 for num in nums])



names = 'this is so fun !'

print(''.join([char for char in names if char not in 'aeiou']))
print([val for val in range(1 ,100) if val%12 == 0])


ans =[[0, 1, 2], [0, 1, 2], [0, 1, 2]] 
def test ():
    print ('hello')
print([[i for i in range(0 ,10)] for i in range(0 , 10)])
fist = {
    "one": "Neil",
    "two": "Young",
}
 
print(f'{fist["one"]} { fist["two"]}')
print('{} {}'.format(fist["one"], fist["two"]))


print(test.__name__)

lambda x:x*2 

nums = [2, 4, 6,5 ,8 ,7,9]
doubles = list(map(lambda x:x*3 , nums))
print(doubles)

print(sys.getsizeof(all(x%2 == 0 for x in nums)) )
print(sys.getsizeof(all([x%2 == 0 for x in nums])))

# sort sort in place whilesorted create a new list or any type, sort work only on list while sorted work also with tuple
# dict also can be used with sorted 
# my_dict = [{}]
# sorted(my_dict , key=len)
# sorted(my_dict , key=lambda user :user['username'])
# sorted(my_dict , key=lambda user :len(user['tweets']) , reverse=True)

print([1,2,3,4,5][2::-1])

from colorama import init
init()
import termcolor

print(termcolor.colored('hello', color='yellow', on_color='on_yellow',attrs=['blink']))


import requests

print(requests.get( 'https://hn.algolia.com/api'))
r = requests.get( 'https://www.google.com/search?q="tom"')

print(f'your request to https://www.google.com came back with status code {r.status_code}')



class hello_name:
    # Initialize a new user with name and age
    def __init__(self,name,age):
        self.name =name
        self.age =age
        
    def print_age(self):
        print(self.name)
        

print(help(hello_name))


comp_tup = [ (1,3),(3,5), (4,7)]

filtered = filter(lambda x: abs(complex(x[0], x[1]))>4 , comp_tup)


mapped = list(map(lambda x: complex(x[0], x[1]) , filtered))

print(filtered)
print(mapped)