import random

def createDraw(names):
    #TODO: Ensure each team has 3 byes and plays 24 games.
    rounds = []

    avaliableForBye = []
    for name in names:
        avaliableForBye.append([name, 0])
        
    for x in range (1,28):
        matches = []
        avaliableTeams = names.copy()

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

        # If there's one team left, add them to a "bye" match
        if len(avaliableTeams) == 1:
            matches.append([avaliableTeams[0], "Bye"])
            
        
        rounds.append(matches)
    return rounds

def generateByes(round, avaliableTeams, avaliableForBye):
    byeTeams = []
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

