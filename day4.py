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

selection = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if selection == 0:
  print(rock)
elif selection == 1:
  print(paper)
elif selection == 2:
  print(scissors)
else:
  print("No such option. Chose 0,1,2")

#Computer selection

random_selection = random.randint(0,2)
print(f"Computer's selection {random_selection}")
if random_selection == 0:
  print(rock)
elif random_selection == 1:
  print(paper)
elif random_selection == 2:
  print(scissors)
else:
  print("No such option. Chose 0,1,2")

if selection == 0 and random_selection == 1:
  print("Computer won")
elif selection == 0 and random_selection == 2:
  print("You won!")
elif selection == 1 and random_selection == 0:
  print("You won!")
elif selection == 1 and random_selection == 2:
  print("Computer Won!")
elif selection == 2 and random_selection == 0:
  print("Computer Won!")
elif selection == 2 and random_selection == 1:
  print("You won!")
else:
  ("Try again!")
