# --------------Read File---------------------
# f=open("text.txt")
# data=f.read()
# print(data)
# f.close()

# --------------Write File---------------------
# st="The random-access memory is volatile, and all its contents are lost once a program terminates. In order topersist the data forever we use files.A file is data stored in a storage device. A python program can talk to the file by reading content from it andwriting content to it"
# f=open("myfile.txt","w")
# f.write(st)
# f.close()

# --------------Readline File---------------------
# st="The random-access memory is volatile, and all its contents are lost once a program terminates. In order topersist the data forever we use files.A file is data stored in a storage device. A python program can talk to the file by reading content from it andwriting content to it"
# f=open("myfile.txt")
# line=f.readline()
# while(line != " "):
#     print(line)
#     line=f.readline()
# f.close()

# --------------append File---------------------
add="my name is ghulam hassan"
f=open("text.txt","a")
a=f.write(add)
print(a)