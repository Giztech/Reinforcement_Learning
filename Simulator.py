from TrackImporter import TrackImporter
from SARSA import SARSA

class Simulator:
    def __init__(self, track, start, velocity, mdp):
        self.track = track
        self.start = start
        self.velocity = velocity
        self.mdp = mdp

    def callSARSA(self):
        sarsa = SARSA(self.mdp)

    def restartBeginning(self):
        pass

    def restartLast(self):
        pass



