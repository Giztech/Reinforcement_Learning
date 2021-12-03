import copy
from SARSA import SARSA
from ValueIteration import ValueIteration
from TrackImporter import TrackImporter
from SARSA import SARSA
from MDP import MDP
import random as rand


class Simulator:
    #  restartStart should be False for every track, except R track for the comparison
    def __init__(self, track, start, velocity, MDP, size, restartStart):
        self.size = size
        self.restartStart = restartStart
        self.mdp = MDP
        self.track = track
        self.start = start
        self.velocity = velocity
        self.timestep = 0
        self.position = rand.choice(track.start)
        self.lastPos = self.position
        # reward is initially -1 because starting is -1
        self.reward = -1

    def restartLastPos(self):
        self.position = self.lastPos
        self.velocity = [0, 0]

    def restartBeginning(self):
        self.position = self.start
        self.velocity = [0, 0]

    def makeAction(self):
        num = rand.randint(0, 4)
        if num == 0:
            return False
        else:
            return True

    #  check to make sure an action is possible (acceleration is okay and the new position would be on the board)
    def checkAction(self, accel):
        newpos = (self.velocity[0] + accel[0], self.velocity[1] + accel[1])
        if (newpos[0]) > 5 or (newpos[1]) > 5 or (newpos[0]) < -5 or (newpos[1]) < -5:
            # if the new acceleration is greater than 5 or less than 5, return false
            return False
        elif newpos[0] >= self.size[0] or newpos[1] >= self.size[1] or newpos[0] < 0 or newpos[1] < 0:
            # if the new acceleration takes it off the board, return false
            return False
        else:
            return True

    def movePos(self, acceleration):
        self.timestep += 1
        self.lastPos = self.position
        if self.makeAction():
            self.velocity[0] += acceleration[0]
            self.velocity[1] += acceleration[1]

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        #  if we land off track
        if self.mdp.R(self.position) == '#':
            if self.restartStart is True:
                self.restartBeginning()
            else:
                self.restartLastPos()
            return None

        #  TODO checking for clipping corners


        return self.mdp.R(self.position)


    def goSARSA(self):
        sarsa = SARSA(self.mdp)
        while True:
            state = (self.position, self.velocity)
            accelerate = sarsa.sarsa(state, newReward)
            newReward = self.movePos(accelerate)


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





