import random

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
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

if user == 0:
    print(f"You choose: {rock}")
elif user == 1:
    print(f"You choose: {paper}")
else:
    print(f"You choose: {scissors}")

computer = random.randint(0,2)
if computer == 0:
    print(f"Computer choose: {rock}")
elif computer == 1:
    print(f"Computer choose: {paper}")
else:
    print(f"Computer choose: {scissors}")
if user == computer:
    print("Tie!")
if user == 0 and computer == 1 or user == 1 and computer == 2 or user == 2 and computer == 0:
    print("You lose!")
if user == 0 and computer == 2 or user == 1 and computer == 0 or user == 2 and computer == 1:
    print("You won!")
