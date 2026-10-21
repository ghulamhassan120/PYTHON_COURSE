a=[11,111,43,56,767,899,323,564]
def greator(a,b):
    if(a>b):
        return a
    return b
from functools import reduce
print(reduce(greator,a))