l=[1,2,3,4,5,6]
sqaure=lambda x:x*x

# map function 
mySql=map(sqaure,l)
print(list(mySql))

# filter function
def even(n):
    if(n%2==0):
        return True
    return False
onlyEnv=filter(even,l)
print(list(onlyEnv))

# reduce function
from functools import reduce
def sum(a,b):
    return a+b

sum1=reduce(sum,l)
print(sum1)