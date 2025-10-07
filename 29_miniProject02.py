# creatina a rock, paper, scissor

import random

item_list = ["Rock", "Paper", "Scissor"]

# taking the user input for game
user_chioce = input("enter your choice (Rock , Paper , Scissor):")

# here we used random library in which ther is a function called choice make a random choice from the sequence
computer_choice = random.choice(item_list)


# getting choice of the users here what user choice and what is computer choice
print(f"User choice is {user_chioce} , computer choice is {computer_choice}")
# making logic to print game results
if user_chioce == computer_choice:
    print("both chooses same , match tie")
elif user_chioce == "Rock":
    if computer_choice == "Paper":
        print("Paper covers the rock , computer win ")
    else:
        print("Rock smash the Scissor , user win ")

elif user_chioce == "Paper":
    if computer_choice == "Rock":
        print("Paper covers the rock , User win ")
    else:
        print("Sessior cut the paper , Computer win ")
elif user_chioce == "Sessior":
    if computer_choice == "Paper":
        print("Sessior cuts the paper , User win ")
    else:
        print("Rock smash the Sessior , Computer win ")

else:
    print("Incorrect input please re-try")

print("GAME OVER !!!")
