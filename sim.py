import random
from team import Team
from match import generateScore
from ladder import printLadder
from draw import createDraw

def main():
    namesFile = open("teams.txt", "r")
    names = [name.strip() for name in namesFile]
    teams = []

    # Initalise up all the team objects
    for name in names:
        teamObject = Team(name, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        teams.append(teamObject)
    
    rounds = createDraw(names)

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
                scores = generateScore()
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
    #TODO: Add finals, add functionality to allow users to see scores per round and see the ladder after each round.
    printLadder(teams)
        
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