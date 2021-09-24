# problem4
'''
import random
you = input("scissors, rock, paper: ")
action = ["scissors", "rock", "paper"]
comp = random.choice(action)
if comp == you:
    print("It is a draw")
if comp == "scissors" and you == "rock":
    print("You won")
if comp == "scissors" and you == "paper":
    print("You lost")
if comp == "rock" and you == "paper":
    print("You won")
if comp == "rock" and you == "scissors":
    print("You lost")
if comp == "paper" and you == "rock":
    print("You lost")
if comp == "paper" and you == "scissors":
    print("You won")
'''
# problem3
import secrets
import string
n = int(input("number: "))
num = string.digits
password = ''.join(secrets.choice(num) for i in range(n))
print(password)