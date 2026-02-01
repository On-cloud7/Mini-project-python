#rock-paper scissor game:
"""_summary_
1- input from user (rock,paper,scissor)
2- computer choice (computer will choose randomly not conditionally)
3- Result print

cases:
A - Rock
Rock - Rock = tie
Rock -paper = Paper wins
Rock -scissor = Rock wins

B - Paper
paper- paper = tie
paper - rock = paper win
paper - scissor = scissor win

C - Scissor
Scissor - Scissor = win
Scissor - Rock = Rock win
Scissor - paper = Scissor wins

    """
import random
item_list = ["rock","paper","Scissor"]
user_choice = input("enter your move = rock,paper,scissor:")
comp_choice = random.choice(item_list)
print(f"user choice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("both chooses same :  = Match tie")
elif user_choice == "rock":
    if comp_choice == "paper":
        print("paper wins : computer wins")
    else:
        print("rock wins : user wins")
        
elif user_choice == "paper":
    if comp_choice == "scissor":
        print("scissor wins : computer wins")
    else:
        print("paper wins : user wins")
elif user_choice == "scissor":
    if comp_choice == "rock":
        print("rock wins : computer wins")
    else:
        print("scissor wins : user wins")