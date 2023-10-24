from team import Team
from match import generateScore
from ladder import printLadder
from draw import createDraw
from format import Format

def main():
    namesFile = open("teams.txt", "r")
    names = [name.strip() for name in namesFile]
    teams = []

    # Initalise all the team objects
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
                scores = generateScore(False)

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

    teams.sort(key=lambda x: (x.points, x.differential),  reverse=True)

    finalsTeams = []
    for x in range(0,8):
        finalsTeams.append(teams[x].name)
    matchesWeekOne = [[finalsTeams[0], finalsTeams[3]], [finalsTeams[1], finalsTeams[2]], [finalsTeams[4], finalsTeams[7]], [finalsTeams[5], finalsTeams[6]]]
    matchesWeekTwo = [[],[]]
    matchesWeekThree = [[],[]]

    print(" ")
    print("Finals Week 1")
    count = 1
    for match in matchesWeekOne:
        print(" ")
        print(Format.underline + (match[0] + "(H) VS " + match[1]) + "(A)" + Format.end)
        
        scores = generateScore(True)
        winnerHome = False
        winnerAway = False

        if scores[0] > scores[1]:
            winnerHome = True
        elif scores[0] < scores[1]:
            winnerAway = True

        print(match[0] + ": " + str(scores[0]))
        print(match[1] + ": " + str(scores[1]))

        if count == 1:
            if winnerHome:
                matchesWeekTwo[0].append(match[1])
                matchesWeekThree[0].append(match[0])
            elif winnerAway:
                matchesWeekTwo[0].append(match[0])
                matchesWeekThree[0].append(match[1])
        elif count == 2:
            if winnerHome:
                matchesWeekTwo[0].append(match[0])
            elif winnerAway:
                matchesWeekTwo[0].append(match[1])
        elif count == 3:
            if winnerHome:
                matchesWeekTwo[1].append(match[0])
            elif winnerAway:
                matchesWeekTwo[1].append(match[1])
        elif count == 4:
            if winnerHome:
                matchesWeekTwo[1].insert(0, match[1])
                matchesWeekThree[1].append(match[0])
            elif winnerAway:
                matchesWeekTwo[1].insert(0, match[0])
                matchesWeekThree[1].append(match[1])
        count += 1
    
    print(" ")
    print("Semi Finals")
    count = 1
    for match in matchesWeekTwo:
        print(" ")
        print(Format.underline + (match[0] + "(H) VS " + match[1]) + "(A)" + Format.end)

        scores = generateScore(True)
        winnerHome = False
        winnerAway = False

        if scores[0] > scores[1]:
            winnerHome = True
        elif scores[0] < scores[1]:
            winnerAway = True

        print(match[0] + ": " + str(scores[0]))
        print(match[1] + ": " + str(scores[1]))

        if count == 1:
            if winnerHome:
                matchesWeekThree[1].append(match[0])
            elif winnerAway:
                matchesWeekThree[1].append(match[1])
        else:
            if winnerHome:
                matchesWeekThree[0].append(match[0])
            elif winnerAway:
                matchesWeekThree[0].append(match[1])
        count += 1
    
    print(" ")
    print("Preliminary Finals")
    grandFinal = []
    for match in matchesWeekThree:
        print(" ")
        print(Format.underline + (match[0] + "(H) VS " + match[1]) + "(A)" + Format.end)

        scores = generateScore(True)
        winnerHome = False
        winnerAway = False

        if scores[0] > scores[1]:
            winnerHome = True
        elif scores[0] < scores[1]:
            winnerAway = True

        print(match[0] + ": " + str(scores[0]))
        print(match[1] + ": " + str(scores[1]))

        if winnerHome:
            grandFinal.append(match[0])
        elif winnerAway:
            grandFinal.append(match[1])
    
    print(" ")
    print("Grand Final")
    print(" ")
    print(Format.underline + (grandFinal[0] + " VS " + grandFinal[1]) + Format.end)

    scores = generateScore(True)
    winnerHome = False
    winnerAway = False

    if scores[0] > scores[1]:
        winnerHome = True
    elif scores[0] < scores[1]:
        winnerAway = True

    print(grandFinal[0] + ": " + str(scores[0]))
    print(grandFinal[1] + ": " + str(scores[1]))

    print(" ")

    if winnerHome:
        print(grandFinal[0].upper() + " WIN THE GRAND FINAL")
    elif winnerAway:
        print(grandFinal[1].upper() + " WIN THE GRAND FINAL")

    

        
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