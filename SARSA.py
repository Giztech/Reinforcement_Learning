import random

class SARSA:
    def __init__(self, mdp):
        self.mdp = mdp
        self.learningRate = .1 #TUNE <.1
        self.discountFactor = 1 #TUNE
        self.epislon = 1 #TUNE
        self.Q = {}
        for s in mdp.states:
            state = {}
            for a in mdp.actions:
                state[tuple(a)] = 0
            self.Q[s] = state
        self.s = None
        self.a = None

    def sarsa(self, currState, reward):
        if self.s != None:
            currAction = self.chooseAction(currState)
            print(self.a)
            print(self.s)
            print(currState)
            print(currAction)
            self.Q[self.s][self.a] += self.learningRate * (reward + (self.discountFactor * self.Q[currState][currAction]) - self.Q[self.s][self.a])
            self.s = currState
            self.a = currAction
        self.s = currState
        currAction = self.chooseAction(currState)
        self.a = currAction
        return self.a

    def chooseAction(self, state):
        if random.random() < self.epislon:
            print(self.Q[tuple(state)])
            action = max(self.Q[state], key=self.Q[state].get)
            print(action)
        else:
            action = random.choice(self.mdp.actions)
            print(action)
        return tuple(action)

