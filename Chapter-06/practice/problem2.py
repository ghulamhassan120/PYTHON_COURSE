marks1=int(input("Enter marks 1: "))
marks2=int(input("Enter marks 2: "))
marks3=int(input("Enter marks 3: "))

# check for total percentage

total_percentage=(100*(marks1+marks2+marks3))/300
print(total_percentage)

if(total_percentage>=40  and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are pass")
else:
    print("Yor failed")