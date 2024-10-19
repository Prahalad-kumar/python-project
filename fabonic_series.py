def fobanici_series(Num):
    if(Num<=0):
        return []
    elif(Num==1):
        return [0]
    elif(Num==2):
        return [0,1]

    fib_series=[0,1]
    while len(fib_series) < Num:
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series



print(fobanici_series(1))


