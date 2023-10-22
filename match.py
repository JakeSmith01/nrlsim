import random

def scoreGenerator():
    homeScore = tryGenerator()
    awayScore = tryGenerator()

    # If scores are level decide if games end in a draw or is won in extra time
    if homeScore == awayScore:
        drew = random.choices([True, False], weights=(5,95))

        # If teams dont draw, decide winning method and winning team
        if drew[0] == False:
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
            return([homeScore, awayScore, True, False])                          #TODO: Fix this return so its just one return. 
        else:                                                                     # Also make it more clear that the third value is if they go to extra time and the last value is if they drew
            return([homeScore, awayScore, True, True])
    else:
        return([homeScore, awayScore, False, False])

def tryGenerator():
    tryScored = random.choices([True, False], weights=(80,20))
    if tryScored[0]:
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
        convertedTries = random.randint(0,tries)
        return((tries * 4) + (convertedTries * 2))
    else:
        return(0)