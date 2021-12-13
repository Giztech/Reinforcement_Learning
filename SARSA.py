import random

class SARSA:
    def __init__(self, mdp):
        self.mdp = mdp
        self.learningRate = .09 #TUNE <.1
        self.discountFactor = .99 #TUNE
        self.epislon = .1 #TUNE
        self.Q = {}
        for s in mdp.states:    #initalizes policy table so every value is 0
            state = {}
            for a in mdp.actions:
                state[tuple(a)] = 0
            self.Q[s] = state
        self.s = None
        self.a = None

    def sarsa(self, currState, reward):
        """"Kieran Ringel
        Selects action based on policy table and updates the policy table"""
        while True:
            currAction = self.chooseAction(currState)   #selects action
            if self.mdp.checkAction(currAction, currState[1], currState[0]):    #if action does not make velocity exceed -5 or 5
                if self.s != None:  #if prev state is not null
                    self.Q[self.s][self.a] += self.learningRate * (reward + (self.discountFactor * self.Q[currState][currAction]) - self.Q[self.s][self.a])
                    #update policy table
                self.s = currState
                self.a = currAction
                return self.a   #returns action

    def chooseAction(self, state):
        """Kieran Ringel
        small probability it selects a random action
        otherwise it selections an action that corresponds to the largest value in the policy table based on the current state"""
        if random.random() < self.epislon:
            action = max(self.Q[state], key=self.Q[state].get)
        else:
            action = random.choice(self.mdp.actions)
        return tuple(action)
