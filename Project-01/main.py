computer=-1
youstr=input("Enter Your Choice")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]

if(computer==you):
    print("it is draw")
else:
    if(computer==-1 and you==1):
        print("You Win!")
    elif(computer==-1 and you==0):
        print("You Loss!")
    elif(computer==1 and you==-1):
        print("You Loss!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Loss!")
    else:
        print("SomeThing went wrong")