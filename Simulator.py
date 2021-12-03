import random
import copy
from SARSA import SARSA
from ValueIteration import ValueIteration


class Simulator:
    def __init__(self, track, start, velocity, mdp):
        self.track = track
        self.start = start
        self.velocity = velocity
        self.mdp = mdp
        self.actions = 0
        self.position = random.choice(start)

    def callSARSA(self):
        sarsa = SARSA(self.mdp)

    def callValueIteration(self):
        vi = ValueIteration()
        vi.maximizePolicy(self.mdp, vi.valueIteration(self.mdp))

    def print_track(self):
        rTrack = copy.deepcopy(self.track)
        rTrack[self.position[0]][self.position[1]]= "C"
        out = "Race Track:\n"
        for x in rTrack:
            out += str(x) + "\n"
        print(out)





