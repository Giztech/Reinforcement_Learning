import copy
from SARSA import SARSA
from ValueIteration import ValueIteration
from TrackImporter import TrackImporter
from SARSA import SARSA
from MDP import MDP
import random as rand


class Simulator:
    #  restartStart should be False for every track, except R track for the comparison
    def __init__(self, track, start, velocity, MDP, size, finish, crashnburn):
        self.size = size
        self.crashnburn = crashnburn
        self.mdp = MDP
        self.track = track
        self.start = start
        self.finish = finish
        self.velocity = velocity
        self.timestep = 0
        self.position = rand.choice(start)
        self.lastPos = self.position
        # reward is initially -1 because starting is -1
        self.reward = -1

    def restartLastPos(self):
        self.position = self.lastPos
        self.velocity = [0, 0]

    def restartBeginning(self):
        self.position = self.start
        self.velocity = [0, 0]

    #  nondeterminism bby
    def makeAction(self):
        num = rand.randint(0, 4)
        if num == 0:
            return False
        else:
            return True

    def movePos(self, acceleration):
        self.timestep += 1
        self.lastPos = self.position

        #  if we can make the action, we increase our velocity
        if self.makeAction():
            self.velocity[0] += acceleration[0]
            self.velocity[1] += acceleration[1]

        #  we update our position based on the velocity
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # yum is the new reward
        yum = self.mdp.Rewards(self.position)
        self.reward += yum
        #  if we land off track it's really bad
        if yum == -10:
            if self.crashnburn is True:
                self.restartBeginning()
            else:
                self.restartLastPos()
            return yum

        #  TODO check for clipping corners


        return yum

    def goSARSA(self):
        sarsa = SARSA(self.mdp)
        newReward = -1
        # iterate over stuff until
        while True:
            state = (tuple(self.position), tuple(self.velocity))
            accelerate = sarsa.sarsa(state, newReward)
            newReward = self.movePos(accelerate)
            if state[0] in self.finish:
                print("WE DONE")
                quit


    def callValueIteration(self):
        vi = ValueIteration()
        vi.maximizePolicy(self.mdp, vi.valueIteration(self.mdp))

    def print_track(self):
        rTrack = copy.deepcopy(self.track)
        rTrack[self.position[0]][self.position[1]] = "C"
        print("Race Track:")
        for x in rTrack:
            for p in x:
                if p != -1:
                    print('', p, end='')
                else:
                    print(p,end='')
            print('\n')





