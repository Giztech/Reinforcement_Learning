
class SARSA:
    def __init__(self, mdp):
        self.mdp = mdp
        self.learningRate = .1 #TUNE <.1
        self.Q = {}
        for s in mdp.states:
            state = {}
            for a in mdp.actions:
                print(tuple(a))
                state[tuple(a)] = 0
            self.Q[s] = state
        print(self.Q)
        self.prevState = None

    def sarsa(self, percept):
        return action