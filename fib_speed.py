import time 

#speed of fib with recursion and recursion with mempory

#mem for fib
def mem(n, m):
    if len(m) < n:
        m.append(fib(n,m))
    return m[n-1]

#fib with mem
def fib(n, m):
    if n<2:
        return 1
    return mem(n-1,m) + mem(n-2,m)

#fib slow way
def fib_slow(n):
    if n<2:
        return 1
    return fib_slow(n-1)+fib_slow(n-2)  

#get start time
start = time.time()

#collect numbers in a list
l=[]
#calculate first 36 fib numbers with slow function
for i in range(36):
    #add next number to the list
    l.append(fib_slow(i))
    #print (fib_slow(i))
#show list of fib numbers
print(l)

#get end time and print it
end = time.time()
print("calc time:", end - start)

#get new start time
start = time.time()

#collect numbers in a list
l=[]
#calculate first 36 fib numbers with mem function
for i in range(36):
    #add next number to the list
    l.append(fib(i, []))
    #print (fib(i, []))
#show list of fib numbers
print(l)

#get end time and print
end = time.time()
print("calc time:", end - start)