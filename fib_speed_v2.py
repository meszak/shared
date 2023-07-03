import time 

#speed of fib with recursion and recursion with mempory

#mem for fib
def mem(n, m):
    #set c as global variable
    global c
    if len(m) < n:
        m.append(fib(n,m))
        #increment counter
        c=c+1
    return m[n-1]

#fib with mem
def fib(n, m):
    if n<2:
        return 1
    return mem(n-1,m) + mem(n-2,m)

#fib slow way
def fib_slow(n):
    #set c as global variable
    global c
    if n<2:
        return 1
    #increment counter
    c=c+1
    return fib_slow(n-1)+fib_slow(n-2)

#get start time
start = time.time()

#collect numbers in a list
l=[]
#set counter to 0
c=0
#calculate first 36 fib numbers with slow function
for i in range(36):
    #add next number to the list
    l.append(fib_slow(i))
    #print (fib_slow(i))
#show list of fib numbers
print(l)

#get end time and print it
end = time.time()
print("calc time:", end - start, " calc counter: ", c)

#get new start time
start = time.time()

#collect numbers in a list
l=[]
#set counter to 0
c=0
#calculate first 36 fib numbers with mem function
for i in range(36):
    #add next number to the list
    l.append(fib(i, []))
    #print (fib(i, []))
#show list of fib numbers
print(l)

#get end time and print
end = time.time()
print("calc time:", end - start, " calc counter: ", c)