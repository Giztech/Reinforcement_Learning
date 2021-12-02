from TrackImporter import TrackImporter
from SARSA import SARSA
from MDP import MDP
from random import random


class Simulator:
    def __init__(self, track, start, velocity):
        self.track = track
        self.start = start
        self.velocity = velocity
        self.actions = 0
        self.postion = random.choice(track.start)



