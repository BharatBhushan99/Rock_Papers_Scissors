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


lst = [rock, paper, scissors]
map_lst = []

try:
  player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) 
  print(lst[player_choice])
  
except:
  print("Incorrect input.")
else:
  print("Computer chose:\n")

  computer_choice = random.randint(0,2)
  print(lst[computer_choice])

  if (lst[player_choice] == rock and lst[computer_choice] == scissors) or (lst[player_choice] == paper and lst[computer_choice] == rock) or (lst[player_choice] == scissors and lst[computer_choice] == paper):
    print("You won!!")
  elif lst[player_choice] == lst[computer_choice]:
    print("It is a tie!!")
  else:
    print("You lost")