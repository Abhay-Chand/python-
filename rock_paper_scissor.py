
import random

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
game_image = [rock,paper,scissors]
user_choice = int(input("What do you choose ?Type 0 for rock ,Type 1 for paper or type 2 for scissors \n"))
print("user choice:")
print(game_image[user_choice])
print("computer choice:")
computer_choice = random.randint(0,2)
print(game_image[computer_choice])
print(f"computer choice: {computer_choice}")
if computer_choice ==0 and user_choice == 2:
    print("You Win!")
elif user_choice >=3:
    print("invalid typing")
elif computer_choice > user_choice:
    print("You Lose!")

elif computer_choice < user_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("Draw!")

 
