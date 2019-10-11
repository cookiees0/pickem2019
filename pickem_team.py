import random


class PickEmTeam:
    def __init__(self, name, rating):
        self._name = name
        self._rating = rating
        self._score = 0
        self._tiebreak = random.uniform(0, 1)

    def get_name(self):
        return self._name

    def get_rating(self):
        return self._rating

    def get_score(self):
        return [self._score, self._tiebreak]

    def eu_ties_man(self):
        self._tiebreak += 1

    def adjust_rating(self, adjustment):
        self._rating += adjustment

    def process_result(self, result, opponent, k=0):
        assert 0 <= k <= 1
        opp_rating = opponent.get_rating()
        opponent.process_result_help(not result, self._rating)
        self.process_result_help(result, opp_rating)

    def process_result_help(self, result, opp_rating, k=0):
        assert 0 <= k <= 1
        self._score += result
        self._rating += k * (result - self._rating / (self._rating + opp_rating)) * (self._rating + opp_rating)

    def expected_score(self, opponent):
        opponent_rating = opponent.get_rating()
        return self._rating / (self._rating + opponent_rating)

