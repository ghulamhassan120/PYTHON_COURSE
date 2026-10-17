with open("log.txt")as f:
    content1=f.read()
with open("poem.txt")as f:
    content2=f.read()

if(content1==content2):
    print("Print Yes these files are indentical")
else:
    print("NO ")