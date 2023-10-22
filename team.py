class Team:
    def __init__(self, name, points, pointsFor, pointsAgainst, differential):
        self.name = name
        self.points = points # Points from games won/drawn
        self.pointsFor = pointsFor # Points scored in games
        self.pointsAgainst = pointsAgainst # Points conceded in games
        self.differential = differential # Difference between points scored/conceded