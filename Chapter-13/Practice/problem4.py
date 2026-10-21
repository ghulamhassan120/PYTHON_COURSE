def divisible(n):
    if(n%5==0):
        return True
    return False

a=[2323,443,232,22,2,22,5]
f=list(filter(divisible,a))
print(f)