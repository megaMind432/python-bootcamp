import random


class Warrior:
    brave = True

    def war(self):
        print("Called by {}".format(self))
        return bool(random.randint(0, 1))
