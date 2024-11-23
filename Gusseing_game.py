import random
n1=random.randint(1,100)
while True:
    n2=int(input("Enter your guess:"))
    if n1==n2:
        print("Your guess is correct")
        break
    elif n1<n2:
        print("Your guess is higher")
    elif n1>n2:
        print("Your guess is lower")