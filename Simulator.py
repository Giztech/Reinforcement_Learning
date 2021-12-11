import copy
from SARSA import SARSA
from ValueIteration import ValueIteration
from TrackImporter import TrackImporter
from SARSA import SARSA
from MDP import MDP
import random as rand
import math


class Simulator:
    #  restartStart should be False for every track, except R track for the comparison
    def __init__(self, track, start, velocity, MDP, size, crashnburn, finish):
        self.size = size
        self.crashnburn = crashnburn
        self.mdp = MDP
        self.track = track
        self.start = start
        self.velocity = velocity
        self.timestep = 0
        self.position = rand.choice(start)
        self.lastPos = self.position
        # reward is initially -1 because starting is -1
        self.reward = -1
        self.finish = finish

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
        # print('before', self.position)
        self.lastPos = self.position

        #  if we can make the action (NONDETERMINISM), we increase our velocity
        if self.makeAction():
            self.velocity[0] += acceleration[0]
            self.velocity[1] += acceleration[1]

        #  we update our position based on the velocity
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        # print('after', self.position)
        i = self.lastPos[0]
        inew = self.position[0]
        j = self.lastPos[1]
        jnew = self.position[1]
        if i - inew == 0:
            slope = i
        elif j - jnew == 0:
            slope = j
        else:
            slope = (i - inew) / (j - jnew)
        b = i - slope * j
        pairs = []

        if abs(i - inew) > 2:
            if i < inew:
                # so this is numbers between last i pos and next i pos
                for k in range(i + 1, inew):
                    pairs.append([k, math.floor((k - b) / slope)])
            else:
                for k in range(inew + 1, i):
                    pairs.append([k, math.floor((k - b) / slope)])
        if abs(j - jnew) > 2:
            if j < jnew:
                # so this is numbers between last i pos and next i pos
                for k in range(j + 1, jnew):
                    pairs.append([math.floor(slope * i + b), k])
            else:
                for k in range(jnew + 1, j):
                    pairs.append([math.floor(slope * i + b), k])

        # to make sure we don't check some pairs more than necessary
        unique_pairs = []
        for x in pairs:
            if x not in unique_pairs:
                unique_pairs.append(x)
        unique_pairs.append([inew, jnew])
        # print('lastpos', self.lastPos)
        # print("position", self.position)
        # print('velocity', self.velocity)
        # print('action',acceleration)
        for p in unique_pairs:
            # print('pair ', p)

            # look at new rewards function and see if this works because of things
            # also, rounding? round up always...(?)
            temp_reward = self.mdp.OtherRewards(p)
            # print(temp_reward)
            if temp_reward == -10:
                if self.crashnburn is True:
                    self.restartBeginning()
                else:
                    self.restartLastPos()
                self.reward += temp_reward
                # print('ya crashed')
                return temp_reward
            elif temp_reward == 0:
                print('YA WON! How exciting. What a fantastic day! ')
                print('REWARDS: ', self.reward, '\nTIMESTEPS: ', self.timestep)
                quit()

        return -1

    def goSARSA(self):
        sarsa = SARSA(self.mdp)
        newReward = -1
        # iterate over stuff until
        while True:
            state = (tuple(self.position), tuple(self.velocity))
            accelerate = sarsa.sarsa(state, newReward)
            newReward = self.movePos(accelerate)

    def callValueIteration(self):
        vi = ValueIteration()
        vi.maximizePolicy(self.mdp, vi.valueIteration(self.mdp))

    def print_track(self):
        rTrack = copy.deepcopy(self.track)
        rTrack[self.position[0]][self.position[1]] = "C"
        print("Race Track:")
        rTrack[4][8] = '3'
        for x in rTrack:
            for p in x:
                if p != -1:
                    print('', p, end='')
                else:
                    print(p, end='')
            print('\n')
