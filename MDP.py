import itertools
import random
import Simulator

class MDP:
    def __init__(self, size, track):
        size = size.split(',')
        locations = list(itertools.product(range(int(size[0])), range(int(size[1]))))
        velocities = list(itertools.product(range(-5, 6), range(-5, 6)))
        self.states = list(itertools.product(velocities, locations))
        self.actions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
        self.prob = .2
        self.discount = 1  # TUNE <1
        self.reward = {}
        self.setRewards(track)
        self.transitions = {}
        self.terminals = []
        self.setTransitions()


    def Transitions(self, state, action):
        """
        Return the possible states of the given state action pair
        """
        return self.transitions[state][action]

    def Rewards(self, state):
        """
        Return the reward of a state
        """
        return self.reward[tuple(state)]

    def setRewards(self, track):
        """
        Looks at the track and sets the rewards and the terminals or finish line for the MDP
        """
        for state in self.states:
            if track[state[0][1]][state[0][0]] == 'F':
                self.terminals.append((state[0][0], state[0][1]))
                self.reward[state] = 0
            elif track[state[0][1]][state[0][0]] == '.' or track[state[0][1]][state[0][0]] == 'S':
                self.reward[state] = -1
            else:
                self.reward[state] = -10

    def setTransitions(self):
     pass