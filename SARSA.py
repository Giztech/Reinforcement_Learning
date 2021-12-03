from random import random

class SARSA:
    def __init__(self, mdp):
        self.mdp = mdp
        self.learningRate = .1 #TUNE <.1
        self.discountFactor = 1 #TUNE
        self.Q = {}
        for s in mdp.states:
            state = {}
            for a in mdp.actions:
                state[tuple(a)] = 0
            self.Q[s] = state
        self.N = {}
        for s in mdp.states:
            state = {}
            for a in mdp.actions:
                state[tuple(a)] = 0
            self.N[s] = state
        self.s = None
        self.a = None

    def sarsa(self, currState, reward):
        if self.s != None:
            currAction = random.choice(self.mdp.actions)
            self.N[self.s][self.a] += 1
            self.Q[self.s][self.a] += self.learningRate * (reward + (self.discountFactor * self.Q[currState][currAction]) - self.Q[self.s][self.a])
            self.s = currState
            self.a = currAction
