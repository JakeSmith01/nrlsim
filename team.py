class Team:
    def __init__(self, name, points, pointsFor, pointsAgainst, differential, played, wins, draws, losses, byes):
        self.name = name
        self.points = points # Points from games won/drawn
        self.pointsFor = pointsFor # Points scored in games
        self.pointsAgainst = pointsAgainst # Points conceded in games
        self.differential = differential # Difference between points scored/conceded
        self.played = played # Games Played
        self.wins = wins # Games Won
        self.draws = draws # Games Drawn
        self.losses = losses # Games Lost
        self.byes = byes # Byes had
        