import random
sysout=random.randint(1,100)

print('welcome to the game!!!')

count=0
num=int(input("predict some number here between 1 to 50\n"))

while num != sysout:
    if num > sysout:
        print("enter number smaller")
    else:
        print ("enter number greater")
    num=int(input("predict some number here\n"))
    count=count+1
else:
    print("you are right !")
    print("the attempt is",count)

