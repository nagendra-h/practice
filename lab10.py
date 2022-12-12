import time
print(time.time())
def timeit(func):
    def timed():
        print(1000)
        print("Before the Timeit decorator")
        ts = time.time()        
        result = func()
        print(result)
        te = time.time()
        minutes, seconds = divmod((te-ts), 60)
        print(minutes,seconds)
        print ("time taken %8.2f"%((te-ts)*10**6))
        print("After the Timeit decorator")
        print(result)
        print(3)
        return result
    print(2)
    print(func)
    print(timed)
    return timed


@timeit
def fib():
    a,b=0,1
    print(4)
    while(1):
        yield a
        a, b=b ,a+b
       
num = int(input("Enter the size for fibonacci series"))
print('dfgsdf')
print(timeit)
fibonacci = fib()
print(fib)
print('heyyy')
for x in range(num):
    print(next(fibonacci))
    
