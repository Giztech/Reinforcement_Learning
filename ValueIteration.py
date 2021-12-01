
#epsilon

class ValueIteration:
    def __init__(self):
        pass

    def valueIteration(self, MDP, epislon):





        return 0

    def maximizePolicy(self, MDP, U):

        pi = {}
        for s in MDP.states:
            pi[s] = max(MDP.actions(s), key=lambda a: self.utility(a,s,U,MDP))
        return pi

    def utility(self, a, s, U, MDP):

        return sum(p * U[s1] for (p,s1) in MDP.T(s,a))
