"""# wap to find the factorial number . by taking input from user.
def factorial_number(number):
    if number<0:
        return "Sorry We cant find the factorial of negative number"
    if number==0 or number==1:
        return 1
    else:
        return number*factorial_number(number-1)

number=int(input("Enter the number to which you want factorial:"))
total=factorial_number(number)

print(f"The factorial of {number} is {total}:")

#wap to find the fabonaic_series till the user given number
def fabonaic_series(num):
    if num==0:
        return []
    elif num==1:
        return[1]
    else:
        fabo_num=[1,2]
        while len(fabo_num)<num:
            fabonic_series=fabo_num[-1]+fabo_num[-2]
            fabo_num.append(fabonic_series)
        return fabo_num
number=int(input("number:"))
fabonic_series=fabonaic_series(number)
print(fabonic_series)
# wap to check is the given number is prime or not
def is_prime(num):
    if num>0:
        if num==1:
            return True
        else:
            for i in range (2,int(num*.5)+1):
                if num%i==0:
                    return False
            return True
    else:
        return False

print(is_prime(int(input("number:"))))"""

#wap to find the gcd and lcm of two number:
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x
def lcm(x,y):
    return (x*y)/gcd(x,y)
a=int(input("Enter the first number"))
b=int(input("Enter the second  number"))
print(gcd(a,b))
print(lcm(a,b))
