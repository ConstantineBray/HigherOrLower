from random import randint

random = randint(1,100)

x = int(input("Input the value # (Higher or Lower):"))

while(x != random):
    if x < random:
        print("Higher!")
        x = int(input("Input the value # (Higher or Lower):"))
    if x > random:
        print("Lower!")
        x = int(input("Input the value # (Higher or Lower):"))
if x == random:
    print("You win!")




