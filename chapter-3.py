# 1 write a program to display a user entered name followed by good morning using input () function.
name=input("Enter your name=")
print(f"Good morning{name}")

#  11 write a program to greeting the user according to time . with user name

import time
# def the greeting function

def greeting(hour,name):
    if 5 <= hour <12:
        print(f"Good morning {name}")
    elif 12 <= hour <18:
        print(f"Good afternoon {name}")
    elif 18 <= hour <22:
        print(f"Good morning {name}")
    else:
        print(f"Good night {name}")

# taking user name as input
name=input("Enter your name=")
# store the value of hour in hour based on current time.
hour=time.localtime().tm_hour
#results
print(greeting(hour,name))

# 2 write a program to fill in a letter template given below with name and date

# importing date from datetime module

from datetime import date


# def the function letter

def letter(date,name):
    print(f"Dear<|{name}|>")
    print("You are selected!")
    print(f"<|{date}|>")
# taking user name
name=input("Enter your name =")
#taking date of today
date=date.today()
print(letter(date,name))

# 3 write a program to detect double space in a string.
def detect_double_spaces(s):
    # Find the first occurrence of double space
    position = s.find("  ")

    if position != -1:
        print("Double space detected at position:", position)
    else:
        print("No double spaces detected.")


# Example usage
input_string = input("Enter a string: ")
detect_double_spaces(input_string)

# 4 replace the double space from 3 with single spaces.
def remove_double_spaces(s):
    # Find the first occurrence of double space
    position = s.find("  ")

    if position != -1:
       return s.replace("  ", " ")
    else:
        return s


# Example usage
input_string = input("Enter a string: ")
print(remove_double_spaces(input_string))


