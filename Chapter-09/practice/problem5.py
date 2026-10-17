words=["donkey","ganda","bad"]

with open("../myfile.txt","r")as f:
    content=f.read()

for word in words:
    print(word)
    contentNew=content.replace(word,"######")

with open("../myfile.txt","w")as f:
    f.write(contentNew)