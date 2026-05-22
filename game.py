'''
A game scoring system
    - kills <= 5 -> score = kills * 100
    - 5 <= kills <== 10 -> = kills * 150 + 150 (bonus)
    - kills >= 10 -> score = kills * 200 + 1500(bonus)
    - If death > kills, score is halved. Calculate final score.
'''

kills = int(input("Enter no. of kills : "))
if kills <= 5 :
    score = kills * 100
    print(score)
elif 5 <= kills <= 10 :
    score = (kills * 150) + 150
    print(score)
elif kills >= 10 :
    score = kills * 200 + 1500
    print(score)