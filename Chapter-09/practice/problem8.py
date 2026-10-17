with open("this.txt")as f:
    content=f.read()
with open("thisCopy.txt","w")as f:
    f.write(content)