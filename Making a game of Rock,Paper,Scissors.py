import random											 
def play_rock_paper_scissors():
    print("Let's play rock, paper, scissors!")
    choice = input("Rock, paper, or scissors? ")
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    if choice == computer_choice:
       	 print("It's a tie! We both chose", choice)
    elif (choice == "rock" and computer_choice == "scissors" or 
          choice == "paper" and computer_choice == "rock" or
          choice == "scissors" and computer_choice == "paper"):
        print("You win! You chose", choice,"and the computer chose", computer_choice)
    else:
      print("You lose! You chose", choice, " the computer chose", computer_choice) play_rock_paper_scissors()
