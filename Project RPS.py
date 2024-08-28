
import random

from tkinter import*
while True:

    print("..... Welcome to RPS Game .....")
    user_score_label = 0
    comp_score_label = 0
    ties_score = 0

    name = input("Enter Your Name : ")
    print(""""
    Winning rules
    1. Paper Vs Rock --> Paper
    2. Rock Vs scissor --> rock
    3. Scissor Vs Paper --> Scissor
    """)
    print()

    choice = int(input("Enter Your Choice 1-3 : "))
    print()
    while choice > 3 or choice < 1:
        choice = int(input("Enter Valid Choice"))

    if choice == 1:
        user_choice_label = "Rock"
    elif choice == 2:
        user_choice_label = "Paper"
    else:
        user_choice_label = "scissor"

    print("Your Choice is : ", user_choice_label)
    print("Its computer turn : ")

    computer = random.randint(1, 3)

    if computer == 1:
        comp_choice_label = "Rock"
    elif computer == 2:
        comp_choice_label = "Paper"
    else:
        comp_choice_label = "Scissor"

    print("computer choice is : ", comp_choice_label)

    if (user_choice_label == "paper" and comp_choice_label == "Rock") or (user_choice_label == "Rock" and comp_choice_label == "Paper"):
        print("Paper Wins")
        result = "Paper"

    elif (user_choice_label == "Rock" and comp_choice_label == "Scissor") or (user_choice_label == "Scissor" and comp_choice_label == "Rock"):
        print("Rock wins ")
        result = "Rock"

    elif user_choice_label == comp_choice_label:
        print("It's Tie ")
        result = "Tie"

    else:
        print("Scissor Wins")
        result = "Scissor"

    if result == "tie":
        ties_score += 1
    elif result == user_choice_label:
        print(name, "Wins")
        user_score_label += 1
    else:
        print("Computer Wins")
        comp_score_label += 1

    print("Scores are : ")
    print(name, "s score is : ", user_score_label)
    print("computer,s score are : ", comp_score_label)
    print("ties are : ", ties_score)

    repeat = input("Do You Want To Play Again...???")
    if repeat == "No" or repeat == "No":
        break

print("......Game Over.....")
print(".... Thanks For Playing....")



