import random
num=int(random.randrange(1, 22))
print("you have to guess the number between 1 to 21")
print("you have 5 chances")
for i in range(5):
    k=int(input("enter the number: "))
    if(k>num):
        print("greater number")
    elif(k<num):
        print("lesser number")
    elif(k==num):
        print("you won the game")
        break
if(k!=num):
    print("you lost the game")
    print("the number is: ",num)
