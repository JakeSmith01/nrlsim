def printLadder(teams):
    teams.sort(key=lambda x: (x.points, x.differential),  reverse=True)
    count = 1

    print("---------Ladder---------")
    print(" ")
    print('{:3} | {:^30} | {:^6} | {:^6} | {:^4} | {:^5} | {:^4} | {:^4} | {:^3} | {:^7} | {:<3}'.format("Pos", "Team", "Played", "Points", "Wins", "Drawn", "Lost", "Byes", "For",
                                                                                                          "Against", "Diff"))
    for team in teams:
        print('{:3} | {:^30} | {:^6} | {:^6} | {:^4} | {:^5} | {:^4} | {:^4} | {:^3} | {:^7} | {:<3}'.format(count, team.name, team.played, team.points, team.wins, team.draws, 
                                                                                                             team.losses, team.byes, team.pointsFor, team.pointsAgainst, 
                                                                                                             team.differential))
        count += 1

