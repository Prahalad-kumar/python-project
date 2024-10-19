def armstrong(number):
    strnum=str(number)
    size=len(strnum)
    result= sum(int(digit) ** size for digit in strnum)
    if result==int(number):
        print("the number is armstrong")
    else:
        print("the number is not armstrong")

number=input("Enter the number:")
armstrong(number)

