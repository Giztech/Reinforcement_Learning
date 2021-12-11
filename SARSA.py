import random

class SARSA:
    def __init__(self, mdp):
        self.mdp = mdp
        self.learningRate = .1 #TUNE <.1
        self.discountFactor = 1 #TUNE
        self.epislon = .5 #TUNE
        self.Q = {}
        for s in mdp.states:
            state = {}
            for a in mdp.actions:
                state[tuple(a)] = 0
            self.Q[s] = state
        self.s = None
        self.a = None

    def sarsa(self, currState, reward):
        while True:
            currAction = self.chooseAction(currState)
            #if self.mdp.checkAction((-1,-1), (2,0), (9,6)):
            if self.mdp.checkAction(currAction, currState[1], currState[0]):
                if self.s != None:
                    self.Q[self.s][self.a] += self.learningRate * (reward + (self.discountFactor * self.Q[currState][currAction]) - self.Q[self.s][self.a])
                self.s = currState
                self.a = currAction
                print(currState, currAction)
                return self.a
            else:
                print('stuck')


    def chooseAction(self, state):
        if random.random() < self.epislon:
            action = max(self.Q[state], key=self.Q[state].get)
        else:
            action = random.choice(self.mdp.actions)
        return tuple(action)

