
from functools import total_ordering


@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)

    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented
g1, g2 = Grade(80, 100), Grade(60, 100)
g1 >= g2, g1 > g2 # (True, True)


@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)

    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)

    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent > other.score_percent
        else:
            return NotImplemented

g1, g2 = Grade(80, 100), Grade(60, 100)

g1 >= g2, g1 > g2, g1 <= g2, g1 < g2 # (True, True, False, False)