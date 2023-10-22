import random

def createDraw(names):
    rounds = []

    avaliableForBye = []
    for name in names:
        avaliableForBye.append([name, 0])
        
    for x in range (1,28):
        matches = []
        avaliableTeams = names.copy()

        # For each round, generate the team that has the bye, based off this update the teams that can be picked for matches and can be picked for byes
        byeResult = generateByes(x, avaliableTeams, avaliableForBye)
        for team in byeResult[0]:
            matches.append([team, "Bye"])
        avaliableTeams = byeResult[1]
        avaliableForBye = byeResult[2]

        while len(avaliableTeams) > 1:
            team = random.choice(avaliableTeams)
            avaliableTeams.remove(team)
            opponent = random.choice(avaliableTeams)
            avaliableTeams.remove(opponent)
            matches.append([team, opponent]) 
        rounds.append(matches)
    return rounds

def generateByes(round, avaliableTeams, avaliableForBye):
    byeTeams = []
    # Number of teams with a bye per round are picked based on actual NRL draw.
    # For each round we pick valid teams and then update the teams that can still be picked for matches and byes based on that.
    if round == 13 or round == 16 or round == 19:
        while len(byeTeams) < 7:
            validTeams = pickTeams(avaliableTeams, avaliableForBye)
            byeTeams.append(validTeams[0])
            avaliableTeams = validTeams[1]
            avaliableForBye = validTeams[2]
    elif round == 14 or round == 17 or round == 20:
        while len(byeTeams) < 3:
            validTeams = pickTeams(avaliableTeams, avaliableForBye)
            byeTeams.append(validTeams[0])
            avaliableTeams = validTeams[1]
            avaliableForBye = validTeams[2]
    else:
        while len(byeTeams) < 1:
            validTeams = pickTeams(avaliableTeams, avaliableForBye)
            byeTeams.append(validTeams[0])
            avaliableTeams = validTeams[1]
            avaliableForBye = validTeams[2]
    return [byeTeams, avaliableTeams, avaliableForBye]

def pickTeams(avaliableTeams, avaliableForBye):
    validTeam = False
    while not validTeam:
        # Randomly generates a team, checks if it can be used for a bye and then updates the amount of byes. If the team has three byes, removes it from the list.
        team = random.choice(avaliableTeams)
        for value in avaliableForBye:
            if value[0] == team:
                validTeam = True
                avaliableTeams.remove(value[0])
                value[1] += 1
                if value[1] == 3:
                    avaliableForBye.remove(value)
                break
    return [team, avaliableTeams, avaliableForBye]

