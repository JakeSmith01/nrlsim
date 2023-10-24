import random

def generateScore(isFinals):
    homeScore = generateTries()
    awayScore = generateTries()
    extraTime = False
    didDraw = False
    
    # If scores are level decide if games end in a draw or is won in extra time
    if homeScore == awayScore:
        drew = random.choices([True, False], weights=(5,95))
        extraTime = True
        # If teams dont draw, decide winning method and winning team
        if drew[0] == False or isFinals:
            winMethod = random.choices(["fg", "try"], weights=(80,20))
            winner = random.choice(["home", "away"])
            if winMethod[0] == "fg":
                if winner == "home":
                    homeScore += 1
                else:
                    awayScore += 1
            else:
                if winner == "home":
                    homeScore += 4
                else:
                    awayScore +=4                   
        else:                                                                   
            didDraw = True
    return([homeScore, awayScore, extraTime, didDraw])

def generateTries():
    # Randomly pick if a team scores or not with the team scoring being 80% likely.
    tryScored = random.choices([True, False], weights=(80,20))
    if tryScored[0]:
        # Randomly pick category and then randomly generate number of tries based on category
        amountScored = random.choices(["small", "moderate", "large", "massive","supermassive"], weights=(35,50,10,4,1))
        if amountScored[0] == "small":
            tries = random.randint(1,2)
        elif amountScored[0] == "moderate":
            tries = random.randint(3,5)
        elif amountScored[0] == "large":
            tries = random.randint(6,7)
        elif amountScored[0] == "massive":
            tries = random.randint(8,10)
        elif amountScored[0] == "supermassive":
            tries = random.randint(11,16)
        # Randomly determine how many tries are converted.
        convertedTries = random.randint(0,tries)
        fgKicked = random.choices([True, False], weights=(5,95))
        goalsKicked = 0
        if fgKicked[0]:
            goalsKickedChoice = random.choices([1, 2, 3], weights=(90, 9, 1))
            goalsKicked = goalsKickedChoice[0]
        return((tries * 4) + (convertedTries * 2) + goalsKicked)
    else:
        return(0)