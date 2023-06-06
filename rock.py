
import random

i_user_choice = 0
i_computer_choice = 0

while i_user_choice < 3 and i_computer_choice < 3:

    print ("1 => rock")
    print ("2 => paper")
    print ("3 => scissors")

    user_choice = int(input())
    computer_choice = random.randint(1, 3)

    if computer_choice == 1 and user_choice == 1:
        print("you: rock and computer: rock")
    elif computer_choice == 2 and user_choice == 2:
        print("you: paper and computer: paper")
    elif computer_choice == 3 and user_choice == 3:
        print("you: scissors and computer: scissors")

    elif computer_choice == 1 and user_choice == 2:
        print("you: paper and computer: rock")
        i_user_choice += 1

    elif computer_choice == 2 and user_choice == 1:
        print("you: rock and computer: paper")
        i_computer_choice +=  1

    elif computer_choice == 3 and user_choice == 1:
        print("you: rock and computer: scissors")
        i_user_choice +=  1


    elif computer_choice == 1 and user_choice == 3:   
        print("you: scissors and computer: rock")
        i_computer_choice += 1

    elif computer_choice == 2 and user_choice == 3 :
        print("you: scissors and computer: papre")
        i_user_choice +=  1

    elif computer_choice == 3 and user_choice == 2:
        print("you: paper and computer: scissors")     
        i_computer_choice +=  1     


if i_computer_choice > i_user_choice :
     print("computer win")

elif i_user_choice > i_computer_choice:
    print("you win")






