from random import *
choices1 = 0
mycount = []
compcount = []
while choices1 <= 5:
    user = input("enter : ")
    computer = choice(["rock","paper","scissors"])
    if user == computer:
        print("its a tie")
    elif user == "rock":
        if computer == "paper":
            print("computer won")
            compcount.append(1)
        else:
            print("you won!")
            mycount.append(1)
    elif user == "paper":
        if computer == "scissors":
            print("computer won")
            compcount.append(1)
        else:
            print("you won!")
            mycount.append(1)
    elif user == "scissors":
        if computer == "rock":
            print("computer won")
            compcount.append(1)
        else:
            print("you won!")
            mycount.append(1)

    choices1 += 1

mycomp,mycount1 = sum(compcount),sum(mycount)
if mycomp > mycount1:
    print(f"Over all the computer has highscore of {mycomp}")

elif mycomp < mycount1:
    print(f"Over all score of yours is higher than the computer {mycount1}...'you won'")

else:
    print(f"you both has same score {mycomp}")
