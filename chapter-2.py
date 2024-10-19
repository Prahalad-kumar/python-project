#write a program to add two number;
def add(a,b):
    sum=a+b
    print(f"The sum of {a} and {b}  is ",sum)
    return sum;

a=float(input("Enter 1 st number="))
b=float(input("Enter 2 nd number="))

add(a,b)

#write a program to find the reminder when a number is divided by z.

def reminder(x,z):
    dividend=x
    divisor =z
    if divisor == 0:
            print("Error: Division by zero is not allowed.")
    else:
        # Calculate the remainder
        reminder = dividend % divisor
        print(f"The reminder of {x} when divided by {z} is  ",reminder)

x=float(input("Number to be divided="))
z=float(input("Number to divide by= "))

reminder(x,z)


#check the type of variable assigned using input() function.

#taking input from user
data=input("Given input=")

#result
print(f"The given input {data} is ",type(data))

#use comparison operator to find out whether 'a' given variable a is greater than 'b' or not.Take a=34 and b=80.

# def the function
def greater_than(a,b):
    if (a>b):
        print(f"{a} is greater than {b}")
    else:
        print(f"{a} is not greater than {b}")
a=float(input("Type the 1st number="))
b=float(input("Type the 2nd  number="))
#using the function
greater_than(a,b)

#write a program to find the average of two numbers entered by the user.

#def the function

def average(a,b):
    avg=(a+b)/2
    return avg

#taking input from user

a=float(input("Enter the 1st number="))
b=float(input("Enter the 2nd number="))

print (f"The average of {a} and {b} is",average(a,b)) #using the function


#write a program to calculate the square of a number entered by the user.

# def the square function
def square(a):
    return a*a

#taking user input
a=int(input("Enter the number="))
print(f"The square of {a} is ",square(a))#calling the function