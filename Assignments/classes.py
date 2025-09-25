"""
this is a program that creates a class called games with a constructor
that gets the sports, teams and no of players in the team.the class is expected to have four objects:
football, basketball, rugby and tennis
"""

class Games:
    def __init__(self, sports, no_teams, no_players):
        self.sports = sports
        self.teams = no_teams
        self.players = no_players

    def __str__(self):
        return f"in{self.sports}, they are self.teams"

football = Games("football", 50, 11)
basketball = Games("basketball", 13, 5)
rugby = Games("rugby", 20, 15)
tennis = Games("tennis", 3, 1)