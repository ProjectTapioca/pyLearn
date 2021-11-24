rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇
import random

#Creating global lists/variables
rps_art = [rock,paper,scissors]
rps_word = ["Rock", "Paper", "Scissors"]

#Code for human input/print
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

print(f"You chose {rps_word[choice]}")
print(rps_art[choice])

#Code for computer choice
comp_choice = random.randint(0,2)

print(f"Computer chose: {rps_art[comp_choice]}")

#If user chooses Rock
if choice == 0:
    if comp_choice == 0:
        print("It's a Draw\n")
    elif comp_choice == 1:
        print("You Lost\n")
    else:
        print("You Win\n")
        
#If user chooses Paper
if choice == 1:
    if comp_choice == 0:
        print("You Win\n")
    elif comp_choice == 1:
        print("It's a Draw\n")
    else:
        print("You Lost\n")
        
#If user chooses Scissors
if choice == 2:
    if comp_choice == 0:
        print("You Lost\n")
    elif comp_choice == 1:
        print("You Win\n")
    else:
        print("It's a Draw\n")
        
#Dr. Angela Solution
#game_images = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])

# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")