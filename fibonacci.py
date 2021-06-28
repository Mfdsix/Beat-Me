def fibo(n, current=1, last=0, it=1):

    # maximum recursion depth exceeded while calling a Python object
    if(n <= 995):
        new = current + last
        newLast = current
        if(it == 1):
            return fibo(n, current, last, 2)
        elif(it < n):
            return fibo(n, new, newLast, it+1)
        else:
            return new
    else:
        if(n == 1 or n == 2):
            return 1
        else:
            arr = [0, 1, 1]
            for i in range(3, n+1):
                arr.append(arr[i-1] + arr[i-2])

            return arr[-1]


print(fibo(1))
print(fibo(995))
print(fibo(10000))
