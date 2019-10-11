import random
import itertools
from typing import List
from pickem_team import PickEmTeam


class PickEmGroup:
    def __init__(self, teams: List[PickEmTeam], group_no="#"):
        self._teams = teams
        self._group_no = group_no
        self._verbose = False

    def set_verbose(self, verbose):
        self._verbose = verbose

    def simulate_group(self):
        for i in range(0, 2):
            for pair in itertools.combinations(self._teams, 2):
                expected_result = pair[0].expected_score(pair[1])
                bless_rng = random.uniform(0, 1)
                result = bless_rng < expected_result
                pair[0].process_result(result, pair[1])
                if self._verbose:
                    print(pair[0].get_name() + "-" + pair[1].get_name() +
                          "\n\tExpected: " + str(expected_result) +
                          "---" + str(bless_rng) + "---" + str(result))

        self._teams.sort(key=lambda x: x.get_score(), reverse=True)

    def get_results(self):
        if self._verbose:
            return [[team.get_name(), team.get_score()] for team in self._teams]
        else:
            return [team.get_name() for team in self._teams]

    def eu_ties(self):
        eu_teams = [team for team in self._teams if team.get_name() in ["Fnatic", "G2 Esports", "Splyce"]]
        for team in eu_teams:
            if self._verbose:
                print("Setting EU ties for " + team.get_name())
            team.eu_ties_man()

    def print_results(self):
        print("Group " + self._group_no + " results: ")
        i = 1
        for team in self._teams:
            wins = team.get_score()[0]
            print(str(i) + ". " + team.get_name() + "(" + str(wins) + "-" + str(6-wins) + ")")
            i += 1

