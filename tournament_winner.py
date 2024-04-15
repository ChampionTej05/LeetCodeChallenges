def tournamentWinner(competitions, results):
    # Write your code here.
    from collections import Counter
    winning_teams = []
    for idx in range(len(competitions)):
        # if results[idx] == 0:
        #     winning_teams.append(competitions[idx][1])

        # else:
        #     winning_teams.append(competitions[idx][0])

        winning_teams.append(competitions[idx][1] if results[idx]==0 else competitions[idx][0])

    
    counter = Counter(winning_teams)
    winner = counter.most_common(1) 
    return winner[0][0]


    
comp = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
res = [0, 0, 1]

print(tournamentWinner(comp, res))

