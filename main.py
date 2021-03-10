import random
import time

n = random.randint(1,3)
playerInput = input("Rock(r), Paper(p) or Scissor(s)? \n")
print("The bot is thinking...")
time.sleep(1)

if n == 1:
  print("Rock!")
  if playerInput == "Paper, p":
    print("You won!")
  else:
      print("You lost!")
if n == 2:
  print("Paper!")
  if playerInput == "Scissor, s":
    print("You won!")
  else:
      print("You lost!")
if n == 3:
  print("Scissor!")
  if playerInput == "Rock, r":
    print("You won!")
  else:
      print("You lost!")