with open("log.txt")as f :
    c=f.read()

if("python" in c):
    print("Yes python is present")
else:
     print("NO python is present")