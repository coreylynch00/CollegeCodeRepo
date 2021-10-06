# Corey Lynch 8/10/2019

team_one = input("What is the name of team 1?")
team_one_goals = input("How many goals did team 1 score?")
team_two = input("What is the name of team 2?")
team_two_goals = input("How many goals did team 2 score?")

if team_one_goals > team_two_goals:
    print(f"{team_one} won the match!")
elif team_one_goals < team_two_goals:
    print(f"{team_two} won the match!")
else:
    print("The match was a draw!")
