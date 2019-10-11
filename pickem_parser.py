import csv
from pickem_team import PickEmTeam


class PickEmParser:
    def __init__(self):
        self._ratings = {}

    def parse_from_tsv(self, filename):
        with open(filename, 'r') as f:
            next(f)
            reader = csv.reader(f, delimiter='\t')
            for team, rating in reader:
                self._ratings[team] = float(rating)

    def _adjust_team_rating(self, team, adjustment):
        self._ratings[team] += adjustment

    def get_pickem_team(self, team):
        return PickEmTeam(team, self._ratings[team])

