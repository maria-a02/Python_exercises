import random

player1 = input("Select Rock, Paper, or Scissor :").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Pikachu used: ", player2)

if player1 == "rock" and player2 == "paper":
    print("Pikachu wins :c")
elif player1 == "paper" and player2 == "scissor":
    print("Pikachu wins :c")
elif player1 == "scissor" and player2 == "rock":
    print("Pikachu wins :c")
if player2 == "rock" and player1 == "paper":
    print("You win ;D")
elif player2 == "paper" and player1 == "scissor":
    print("You win ;D")
elif player2 == "scissor" and player1 == "rock":
    print("You win ;D")
elif player1 == player2:
    print("Tie :O")