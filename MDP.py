import itertools
import random

class MDP:
    def __init__(self, size, track,start):
        self.size = size.split(',')
        self.locations = list(itertools.product(range(int(self.size[0])), range(int(self.size[1]))))
        velocities = list(itertools.product(range(-5, 6), range(-5, 6)))
        self.states = list(itertools.product(self.locations, velocities))
        self.actions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
        self.prob = .2
        self.start = start
        self.discount = 1  # TUNE <1
        self.reward = {}
        self.terminals = []
        self.setRewards(track)
        self.transitions = {}
        self.setMDP()
        self.otherRewards = {}
        self.setOtherRewards(track)

    def Transitions(self, state, action):
        """
        Return the possible states of the given state action pair
        """
        return self.transitions[state][action]

    def OtherRewards(self, state):
        if tuple(state) not in self.otherRewards.keys():
            return -10
        else:
            return self.otherRewards[tuple(state)]

    def Rewards(self, state):
        """
        Return the reward of a state
        """
        return self.reward[state]

    def setOtherRewards(self, track):
        for loc in self.locations:
            i = loc[0]
            j = loc[1]
            if track[i][j] == 0:
                self.otherRewards[loc] = 0
            elif track[i][j] == -1:
                self.otherRewards[loc] = -1
            else:
                self.otherRewards[loc] = -10

    def setRewards(self, track):
        """
        Looks at the track and sets the rewards and the terminals or finish line for the MDP
        """
        for state in self.states:
            if track[state[0][0]][state[0][1]] == 0:
                self.terminals.append((state[0][0], state[0][1]))
                self.reward[state] = 0
            elif track[state[0][0]][state[0][1]] == -1:
                self.reward[state] = -1
            else:
                self.reward[state] = -10


    def setMDP(self,crash = False):
        actions = [-1, 0, 1]
        for state in self.states:
            action = {}
            # Iterate though all possible combinations of actions
            for actionY in actions:
                for actionX in actions:
                    # Change velocity based on action. Velocity must be between -5 and 5
                    velocityX = state[1][0] + actionX
                    if abs(velocityX) > 5:
                        velocityX = state[1][0]
                    velocityY = state[1][1] + actionY
                    if abs(velocityY) > 5:
                        velocityY = state[1][1]
                    # The new position based on action and state
                    sToSPrimeX = state[0][0] + velocityX
                    sToSPrimeY = state[0][1] + velocityY
                    finalStates = []

                    #Bryn
                    #postion, value = FUNCTION(state[0], (sToSPrimeX,sToSPrimeY))


    #  check to make sure an action is possible (acceleration is okay and the new position would be on the board)
    def checkAction(self, accel, velocity, currpos):
        newaccel = (velocity[0] + accel[0], velocity[1] + accel[1])
        newpos = (currpos[0] + newaccel[0], currpos[1] + newaccel[1])
        if (newaccel[0]) > 5 or (newaccel[1]) > 5 or (newaccel[0]) < -5 or (newaccel[1]) < -5:
            # if the new acceleration is greater than 5 or less than 5, return false
            return False
        # elif newpos[0] >= int(self.size[0]) or newpos[1] >= int(self.size[1]) or newpos[0] < 0 or newpos[1] < 0:
        #     # if the new acceleration takes it off the board, return false
        #     return False
        else:
            return True



