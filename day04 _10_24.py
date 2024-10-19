class check_number:
    def prime_num(num):
        if num==1:
            return print(f"The input number {num} is Not prime number")
        for i in range (2,int(num*.5)+1):
            if num%i==0:
                return print(f"The input number {num} is Not  prime number")
        return print(f"The input number {num} is prime number")
    def even_number(num):
        if num%2==0:
            return print(f"The input number {num} is even number")
        else:
            return print(f"The input number {num} is Not even  number")
    def odd_num(num):
        if num%2==1:
            return print(f"The input number {num} is Odd number")
        else:
            return print(f"The input number {num} is prime number")

num=int(input("Enter the number:"))
check_number.even_number(num)
check_number.odd_num(num)
check_number.prime_num(num)