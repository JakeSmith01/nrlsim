import random

def createDraw(names):
    #TODO: Ensure each team has 3 byes and plays 24 games.
    rounds = []
    for x in range (1,28):
        matches = []
        avaliableTeams = names.copy()

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