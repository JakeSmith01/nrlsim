import random
from team import Team
from match import scoreGenerator
from ladder import ladder

def main():
    namesFile = open("teams.txt", "r")
    names = [name.strip() for name in namesFile]
    teams = []

    # Initalise up all the team objects
    for name in names:
        teamObject = Team(name, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        teams.append(teamObject)
    
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

    for round in rounds:
        for match in round:
            # If team has a bye, they dont play a real team and just get two points.
            if match[1] == "Bye":
                for x in teams:
                    if x.name == match[0]:
                        x.points += 2
                        x.byes += 1
                        break
            else:
                scores = scoreGenerator()
                #TODO: Is there a better way to format the extra time? Is it necessary?
                # if scores[2]:
                #     print("Extra Time!")
                # print(match[0] + ": " + str(scores[0]))
                # print(match[1] + ": " + str(scores[1]))
                # print(" ")
                
                #TODO: See if there is a better way to do this.
                homeUpdated = False
                awayUpdated = False

                for x in teams:
                    if x.name == match[0]:
                        updateStats(x, scores[0], scores[1])
                        homeUpdated = True
                    elif x.name == match[1]:
                        updateStats(x, scores[1], scores[0])
                        awayUpdated = True
                    if homeUpdated and awayUpdated:
                        break
    
    ladder(teams)
        
def updateStats(team, pointsFor, pointsAgainst):
    team.pointsFor += pointsFor
    team.pointsAgainst += pointsAgainst
    team.differential = team.pointsFor - team.pointsAgainst
    if pointsFor > pointsAgainst:
        team.wins += 1
        team.points += 2
    elif pointsFor < pointsAgainst:
        team.losses += 1
    else:
        team.draws += 1
        team.points += 1
    team.played += 1

main()