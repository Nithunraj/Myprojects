import random

word_list = ["secret","information","kitchen","Accompany","knee","Accomplish","knife","Acknowledge","knock"]
word = random.choice(word_list).lower()

guess_count = 7
guessed = []

done = False

#prints the word 
#input from user
while not done:
    for letter in word:
        if letter in guessed:
            print(letter,end=" ")
            
        else:
            print("_",end=" ")

    print(" ")
    #guess should run until while gets done
    #guess id kept inside the loop
    guess = input(f"You have left {guess_count} turns, Next choice: ").lower()
    guessed.append(guess)
    if guess not in word or guess == "":
        guess_count -= 1
        if guess_count == 0:
            break
    
    done = True
    #this loop makes the while loop not to break    
    #if guessed is wrong
    for letter in word:
        if letter not in guessed:
            done = False

if done:
    print(f"You found the word '{word}' ,you won!!")

else:
    print(f"You lose ,the word is '{word}'")
