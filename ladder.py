def ladder(teams):
    teams.sort(key=lambda x: (x.points, x.differential),  reverse=True)

    print("---------Ladder---------")
    print(" ")
    for team in teams:
        print('{:30} | {:^2} | {:^4} | {:^4} | {:^4}'.format(team.name, team.points, team.pointsFor, team.pointsAgainst, team.differential))

