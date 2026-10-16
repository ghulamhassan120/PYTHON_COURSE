def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n
l=["Hassan","ALi","raza","an"]

print(rem(l,"an"))