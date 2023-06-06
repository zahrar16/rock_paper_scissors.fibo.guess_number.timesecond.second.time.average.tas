import random

computer_number = random.randint(10, 40)
i = 0

for i in range(1, 11):  
    user_number = int(input("enter yur nummber")) 
    i = i+1

    if computer_number == user_number:
        print("حدست درست بود ")
        print(" you win")
        print("😎👏")
        print("bad",i-1,"bar barnde shodi")
        break

    elif computer_number > user_number:
        print ("برو بالاتر")   
        print ("go up")
        print ("⬇⬇") 

    elif computer_number < user_number:
        print ("برو پایین تر") 
        print (" go down")
        print ("⬆⬆")   