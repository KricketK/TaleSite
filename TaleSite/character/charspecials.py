import random


class Special(object):
    def __init__(self, healbonus=0, attbonus=0, defbonus=0):
        self.healbonus = healbonus
        self.attbonus = attbonus
        self.defbonus = defbonus


class Cunning(Special):
    def __init__(self, *args, **kwargs):
        super(Cunning, self).__init__(*args, **kwargs)
        self.attbonus = random.randint(1, 5)

    def __str__(self):
        return "Cunning adds a bonus to attack."


class Pureblood(Special):
    def __init__(self, *args, **kwargs):
        super(Pureblood, self).__init__(*args, **kwargs)
        self.healbonus = random.randint(1, 5)

    def __str__(self):
        return "Pureblood increases health."


class Thickskin(Special):
    def __init__(self, *args, **kwargs):
        super(Thickskin, self).__init__(*args, **kwargs)
        self.defbonus = random.randint(1, 5)

    def __str__(self):
        return "Thickskin increases defense."
