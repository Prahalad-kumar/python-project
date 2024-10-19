# wap to check the prime number.
# define the function
def Prime_number(n):
    if n==1 : # checking the value if its "1" then return false
        return False
    for i in range(2,int(n*0.5)+1): # the loop check the divisial property frmo 2 to n/2.
        if n%i==0:  # its condition check that if number is divisial by 2 ..... n/2.
            return False
            #if tis divisioal then its return false
    return True
    # its return true of no is not divisable.
print(Prime_number(int(input("Enter the number:"))))
# the function is called . in parameter its take the input from user.

def sum(x,y):
    return x+y

x=int(input("Enter the first Number:"))
y=int(input("Enter the second Number:"))
sum=sum(x,y)
print(f"The sum of number {x} and {y} is {sum} ")

def square_num(num):
    return num*num

num=int(input("Enter the number:"))
squ=square_num(num)
print(f"The square of {num} is {squ}")

def factorial_num(num):
    if num<0:
        return "Not posible it is only for positive integer"
    elif num==0 or num==1:
        return 1
    else:
        return num*factorial_num(num-1)


num=int(input("Enter the number:"))
facto=factorial_num(num)
print(f"The factotial of {num} is {facto}")

def is_leapyear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year=int(input("Enter the year:"))
if is_leapyear(year):
    print(f"The {year} is Leap year")
else:
    print(f"The {year} is not leap year")

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
a=int(input("Enter the First number:"))
b=int(input("Enter the Second number:"))
gcd=gcd(a,b)
print(f"The gcd of {a} and {b}: {gcd}")

def lcm(a,b):
    multiple=max(a,b)
    while True:
        if multiple%a==0 and multiple%b==0:
            return multiple
        multiple +=1
a= int(input())
b=int(input())
lcm=lcm(a,b)
print(lcm)
