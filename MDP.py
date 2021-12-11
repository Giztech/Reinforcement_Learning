import itertools
import math
import random


class MDP:
    def __init__(self, size, track, start):
        self.size = size.split(',')
        self.locations = list(itertools.product(range(int(self.size[0])), range(int(self.size[1]))))
        self.velocities = list(itertools.product(range(-5, 6), range(-5, 6)))
        self.states = list(itertools.product(self.locations, self.velocities))
        self.actions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
        self.prob = .2
        self.start = start
        self.otherRewards = {}
        self.setOtherRewards(track)
        self.discount = 1  # TUNE <1
        self.mdpHigh = .7 # TUNE
        self.mdpLow = .3 # TUNE
        self.reward = {}
        self.terminals = []
        self.setRewards(track)
        self.transitions = {}
        self.statesvi = {}
        self.setStatesVi()
        self.setMDP()

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

    def Actions(self, state):
        #print(state)
        #print(self.transitions[tuple(0,0)])
        return self.transitions[state]

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

    # this creates the valid state, velocity pairs
    def setStatesVi(self):
        validlocations = []
        for loc in self.locations:
            rew = self.otherRewards[loc]
            if rew == -1 or rew == 0:
                validlocations.append(loc)

        self.statesvi = list(itertools.product(validlocations, self.velocities))

    def setMDP(self, crashnburn=False):
        actions = [-1, 0, 1]
        for state in self.statesvi:
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

                    # Bryn
                    position, value = self.checkPos(state[0], (sToSPrimeX, sToSPrimeY))

                    # Go to Start Crash Type
                    if crashnburn:
                        # Car hits wall
                        if value == -1:
                            finalStates.append((self.mdpHigh, (random.choice(self.start), (0, 0))))
                        # Car hits finish
                        elif value == 0:
                            finalStates.append((self.mdpHigh, (position, (0, 0))))
                        # Car hits neither
                        else:
                            finalStates.append((self.mdpHigh, ((sToSPrimeX, sToSPrimeY), (velocityX, velocityY))))
                        # Check for failure
                        position, value = self.checkPos(state[0], (state[0][0] + state[1][0], state[0][1] + state[1][1]))
                        # Car hits wall
                        if value == -1:
                            finalStates.append((self.mdpLow, (random.choice(self.start), (0, 0))))
                        # Car hits finish
                        elif value == 0:
                            finalStates.append((self.mdpLow, (position, (0, 0))))
                        # Car hits neither
                        else:
                            finalStates.append((self.mdpLow, (position, state[1])))
                    # Stop when hitting Wall Crash Type
                    else:
                        # Car hits wall or finish
                        if value == -1 or value == 0:
                            finalStates.append((self.mdpHigh, (position, (0, 0))))
                        # Car hits neither
                        else:
                            finalStates.append((self.mdpHigh, ((sToSPrimeX, sToSPrimeY), (velocityX, velocityY))))
                        # Check for failure
                        position, value = self.checkPos(state[0], (state[0][0] + state[1][0], state[0][1] + state[1][1]))
                        # Car hits wall or finish
                        if value == -1 or value == 0:
                            finalStates.append((self.mdpLow, (position, (0, 0))))
                        # Car hits neither
                        else:
                            finalStates.append((self.mdpLow, (position, state[1])))

                    action[(actionX, actionY)] = finalStates
                self.transitions[state] = action


    def makePairs(self, newPos, currPos):
        pairs = []
        first = max(newPos[0], currPos[0])
        second = min(newPos[0], currPos[0])
        for i in range(second, first):
            pairs.append([i, newPos[1]])
        return pairs

    def checkPos(self, currPos, newPos):
        i = currPos[0]
        inew = newPos[0]
        j = currPos[1]
        jnew = newPos[1]
        undef = False
        pairs = []
        if j - jnew == 0:
            undef = True
            pairs = self.makePairs(newPos, currPos)
        elif i - inew == 0:
            slope = 0
        else:
            slope = (i - inew) / (j - jnew)

        if not undef:
            b = i - slope * j

            # print("b", b, 'slope', slope)
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
                        pairs.append([math.floor(slope * k + b), k])
                else:
                    for k in range(jnew + 1, j):
                        pairs.append([math.floor(slope * k + b), k])

        # to make sure we don't check some pairs more than necessary
        unique_pairs = []
        for x in pairs:
            if x not in unique_pairs:
                unique_pairs.append(x)
        unique_pairs.append([inew, jnew])

        for p in unique_pairs:
            temp_reward = self.OtherRewards(p)
            if temp_reward == -10:
                # if it hits a wall
                return newPos, -1
            elif temp_reward == 0:
                # if it passes the finish line!
                return newPos, 0
        # if it just continues along the path, like the good little car that it should be
        return newPos, 1

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
