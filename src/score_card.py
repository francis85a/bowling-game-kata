class ScoreCard:
    def __init__(self, score_string):
        self.rolls = self._parse_rolls(score_string)

    def _parse_rolls(self, s):
        values = []
        for char in s:
            if char == "X":
                values.append(10)
            elif char == "/":
                values.append(10 - values[-1])
            elif char == "-":
                values.append(0)
            else:
                values.append(int(char))
        return values

    def score(self):
        total = 0
        roll_index = 0
        
        for _ in range(10):
            if self._is_strike(roll_index):
                total += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                total += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                total += self._sum_open_frame(roll_index)
                roll_index += 2
        return total

    def _is_strike(self, index):
        return self.rolls[index] == 10

    def _is_spare(self, index):
        return self.rolls[index] + self.rolls[index + 1] == 10

    def _strike_bonus(self, index):
        return self.rolls[index + 1] + self.rolls[index + 2]

    def _spare_bonus(self, index):
        return self.rolls[index + 2]

    def _sum_open_frame(self, index):
        return self.rolls[index] + self.rolls[index + 1]