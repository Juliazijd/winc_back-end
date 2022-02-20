# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'


# Add your code after this line
class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
        self.check_value()

    def check_value(self):
        if ((self.speed < 0 or self.speed > 1) or
                (self.endurance < 0 or self.endurance > 1) or
                (self.accuracy < 0 or self.accuracy > 1)):
            raise ValueError('value should be between 0 and 1')

    def introduce(self):
        return f'Hello everyone, my name is {self.name}.'

    def strength(self):
        skills = {
            'speed': self.speed,
            'endurance': self.endurance,
            'accuracy': self.accuracy
        }
        strength = max(skills, key=skills.get)
        highest_value = max(skills.values())
        return (strength, highest_value)


class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        speed = getattr(player, 'speed')
        endurance = getattr(player, 'endurance')
        accuracy = getattr(player, 'accuracy')
        return speed + endurance + accuracy

    def compare_players(self, pl1, pl2, skill):
        pl1_skill = getattr(pl1, skill)
        pl2_skill = getattr(pl2, skill)

        if pl1_skill > pl2_skill:
            return getattr(pl1, 'name')
        elif pl1_skill < pl2_skill:
            return getattr(pl2, 'name')
        elif pl1.strength()[1] > pl2.strength()[1]:
            return getattr(pl1, 'name')
        elif pl1.strength()[1] < pl2.strength()[1]:
            return getattr(pl2, 'name')
        else:
            return 'These two players might as well be twins!'


julia = Player('Julia', 0.8, 0.6, 0.3)
bono = Player('Bono', 0.3, 0.6, 0.4)
ray = Commentator('Ray Hudson')

julia
julia.introduce()
ray.name
ray.sum_player(julia)
ray.compare_players(julia, bono, 'endurance')
