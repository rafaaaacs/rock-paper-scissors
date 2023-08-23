import os
import random
import colorama
from colorama import Fore, Back, Style

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

choices = ["Rock", "Paper", "Scissors"]
random.shuffle(choices)

print(Fore.RED + """

                                ██████╗  █████╗ ███████╗ █████╗  ██████╗███████╗      
                                ██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝      
                                ██████╔╝███████║█████╗  ███████║██║     ███████╗█████╗
                                ██╔══██╗██╔══██║██╔══╝  ██╔══██║██║     ╚════██║╚════╝
                                ██║  ██║██║  ██║██║     ██║  ██║╚██████╗███████║      
                                ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝    
                                                                              
    

     """)


user_choice = input(Fore.RESET + Fore.LIGHTRED_EX + "Rock, Paper, or Scissors: ").capitalize()
computer_choice = random.choice(choices)

print(Fore.RESET + Fore.LIGHTRED_EX + "Computer chose: " + computer_choice)

if user_choice in choices:
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print(Fore.GREEN + "You win!")
    else:
        print(Fore.RESET + Fore.RED + "Computer wins!")
else:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")

input(Fore.RESET + "Press Enter to exit...")
