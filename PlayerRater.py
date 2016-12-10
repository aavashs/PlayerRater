
'''Write a function points_calc that takes a players goals and assists and returns their points'''
def points_calc(goals, assists):
    return goals + assists




'''Write a function points_per_game that takes a players points and games played and returns their ppg'''
def points_per_game(points,games):
    return points / games


'''Write a function rate_player that takes a players ppg. If their ppg is greater than 1, return a string
good. If their ppg is greater than 1.28, return a string that says superstar. Otherwise return a string
that says scrub'''
def rate_player(ppg):
    if ppg > 1.28:
        return "He is a superstar"
    elif ppg > 1.0:
        return "He is good"
    else:
        return "Scrub"

'''Now print whether these players are good or not by calling your function
Sidney Crosby = 36 goals 49 assists, 80 games played
Connor McDavid = 16 goals 32 assists, 45 games played
Mark Scheifele = 29 goals 32 assists, 71 games played
Ryan Johanssen = 14, 46, 80 games
Bo Horvat = 16, 24, 82 games
'''

'''Make A Big Dictionary Of Players like this: {name:Name, goals: goals, assists: assists, gamesPlayed: gamesPlayed} }
'''

'''
Loop through the entire array of dictionaries and Print each player's name, goals, assists and games played
'''
print("Connor McDavid")
print(rate_player(points_per_game(points_calc(16,32),45)))

print("\nSidney Crosby")
print(rate_player(points_per_game(points_calc(36,49),80)))

print("\nMark Scheifele")
print(rate_player(points_per_game(points_calc(29,32),71)))

print("\nRyan Johanssen")
print(rate_player(points_per_game(points_calc(14,46),80)))

print("\nBig B")
print(rate_player(points_per_game(points_calc(16,24),82)))

print("\nPatrick Kane")
print(rate_player(points_per_game(points_calc(46,60),82)))

players= [{'name':'Connor McDavid', 'goals':16, 'assists':32, 'gamesPlayed':45}, {'name': 'Sidney Crosby', 'goals':36, 'assists':49, 'gamesPlayed':80}, {'name': 'Mark Scheifele', 'goals':29, 'assists':32, 
'gamesPlayed':71}, {'name': 'Ryan Johanssen', 'goals':14, 'assists':46, 'gamesPlayed': 80}, {'name': 'Big B', 'goals':16, 'assists':24, 'gamesPlayed':82}, {'name': 'Patrick Kane', 'goals':46, 'assists':60, 
'gamesPlayed':82}]

for p in players:
    print (p)
