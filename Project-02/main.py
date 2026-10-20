import random
m=random.randint(1,100)
a=-1
guesses=0

while(a!=m):
    guesses+=1
    a=int(input("Guess the Number : "))
    if(a>m):
        print('Lower Number Please')
    else:
        print('Higher Number Please')

print(f"You have guesses the number correctly in {guesses} attempt")