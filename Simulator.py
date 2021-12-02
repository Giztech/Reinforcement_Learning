from SARSA import SARSA
from random import random


class Simulator:
    def __init__(self, track, start, velocity, mdp):
        self.track = track
        self.start = start
        self.velocity = velocity
        self.mdp = mdp
        self.actions = 0
        self.postion = random.choice(track.start)

    def callSARSA(self):
        sarsa = SARSA(self.mdp)





