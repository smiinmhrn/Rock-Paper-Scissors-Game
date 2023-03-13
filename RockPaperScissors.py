# programer Samin Mehran :)
import random
from os import system, name

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def startGame() :

    print("\033[0;34m" + "[GAME STARTED]" + "\033[0m")

    print("---+---+---+---")
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    print("---+---+---+---")

    randnumber = random.randint(0,2)

    if randnumber == 0 :
        computermove = "rock"
    elif randnumber == 1 :
        computermove = "paper"
    elif randnumber == 2 :
        computermove  = "scissors"


    player1 = input("Hey! make your move :").lower()

    while True :
        
        if player1 == "rock" or player1 == "r" :
            break
        elif player1 == "paper" or player1 == "p" :
            break
        elif player1 == "scissors" or player1 == "s" :
            break  
        else :
            print("\033[0;31m" + "something went wrong !" + "\033[0m")
            player1 = input("Try again : ").lower()

    print(f"computer! make your move :{computermove}")
    player2 = computermove


    if player1 == player2:
        print("\n" + "\033[0;32m" + "that is a tie ..." + "\n" + "\033[0m")

    if player1 == "r" and player2 == "rock" :
        print("\n" + "\033[0;32m" + "that is a tie ..." + "\n" + "\033[0m")

    if player1 == "p" and player2 == "paper" :
        print("\n" + "\033[0;32m" + "that is a tie ..." + "\n" + "\033[0m")    

    if player1 == "s" and player2 == "scissors" :
        print("\n" + "\033[0;32m" + "that is a tie ..." + "\n" + "\033[0m")

    if player1 == "rock" or player1 == "r":
        if player2 == "scissors":
            print("\n" +"\033[0;32m" + "You wined !..." + "\033[0m"+ "\n")

        elif player2 == "paper":
            print("\n" +"\033[0;32m" + "computer wined !..." + "\033[0m"+ "\n")

    if player1 == "paper" or player1 == "p":
        if player2 == "rock" :
            print("\n" +"\033[0;32m" + "You wined !..." + "\033[0m"+ "\n")

        elif player2 == "scissors":
            print("\n" +"\033[0;32m" + "computer wined !..." + "\033[0m"+ "\n")

    if player1 == "scissors" or player1 == "s":
        if player2 == "paper":
            print("\n" +"\033[0;32m" + "You wined !..." + "\033[0m"+ "\n")
        elif player2 == "rock":
            print("\n" +"\033[0;32m" + "computer wined !..." + "\033[0m"+ "\n")
    
    restartGame()

def restartGame() :

    print("---+---+---+---")
    print("\u001b[36m" + "1. Restart game" + "\u001b[0m")
    print("\u001b[36m" + "2. Exit" + "\u001b[0m")
    print("\u001b[36m" + "Make your choice : " + "\u001b[0m")
    choice = input()

    while True:
        
        if choice == "1" :
            clear()
            startGame()
            break
        elif choice == "2" : 
            clear()
            break
        else :
            print("\033[0;31m" + "Wrong command. Try again : " + "\033[0m")
            choice = input()


print("\n" + "\u001b[36m" + "Wellcome ! in this game you can play Rock , paper , Scissors with computer :) " + "\u001b[0m")
print("\u001b[36m" +"You can simply use ")
print("\u001b[36m" +"R => Rock")
print("\u001b[36m" +"P => Paper")
print("\u001b[36m" +"S => Scissors"+ "\u001b[0m" + "\n")
startGame()

    