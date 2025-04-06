#RPS.py
#Name:ANTONIO
#Date: APRIL 6
#Assignment:LAB 3
import random
def main():
  wins = 0
  ties = 0
  losses = 0
  playAgain = "y"
  while playAgain == "y":
    computer = random.choice(["r", "p", "s"])
    player = input("Pick your weapon (r, p, s): ")

    if computer == "r":
      print("Computer chose rock")
    elif computer == "p":
      print("Computer chose paper")
    elif computer == "s":
      print("Computer chose scissors")

    if player == "r":
      print("Player chose rock")
    elif player == "p":
      print("Player chose paper")
    elif player == "s":
      print("Player chose scissors")
    else:
      print("Wrong choice, choose r, p, or s.")
      

    # Game logic
    if player == computer:
      print("It's a tie!")
      ties = ties + 1
    elif player == "r" and computer == "s":
      print("You win!")
      wins = wins + 1
    elif player == "p" and computer == "r":
      print("You win!")
      wins = wins + 1
    elif player == "s" and computer == "p":
      print("You win!")
      wins = wins + 1
    else:
      print("Computer wins!")
      losses = losses + 1

    playAgain = input("Would you like to play again? (y/n): ")



  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
 #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  # #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.
  # #In the end, print the stats