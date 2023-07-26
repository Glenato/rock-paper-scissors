import random

rock = 1
paper = 2
scissors = 3

while True:
    num= random.randint(1,3)
    #print (num)

    choosen = input ("If you want to quit this programme press A and enter.\nChoose between rock 🪨 (1), paper 📄 (2) or scisors ✂️ (3) :\n")
    if choosen.lower =="a":
        break
    elif choosen == "rock" or choosen =="1":
        choosen = "rock"
    elif choosen == "paper" or choosen =="2":
        choosen = "paper"
    elif choosen == "scissors" or choosen =="3":
        choosen = "scissors"
    else:
        print ("Error1")
    
    if  num ==1:
        num = "rock"
    elif num ==2:
        num = "paper"
    elif num ==3:
        num = "scissors"
    
    if num == choosen:
        print (f"The computer and you choose {choosen}")
    elif num == "rock" and choosen == "paper" or num == "paper" and choosen == "scissors" or num == "scissors" and choosen== "rock":
        print (f"You choose {choosen}, and the computer choose {num}, so you win !")    
    elif choosen == "rock" and num == "paper" or choosen == "paper" and num == "scissors" or choosen == "scissors" and num== "rock":
        print (f"You choose {choosen}, and the computer choose {num}, so you lose ...")
    else: 
        print ("Error 2")
    play_again = input ("Do you want to play again ?\nPress Y to replay or just press enter to quit.\n")
    if play_again.lower == "y":
        break
    
