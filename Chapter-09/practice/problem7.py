with open("log.txt")as f :
    lines=f.readlines()

lineno=1
for line in lines:
    if("python" in line):
        print(f"Yes python is present Line NUmber {lineno}")
        break
    lineno+=1
else:
     print("NO python is present")