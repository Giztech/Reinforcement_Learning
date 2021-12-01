
#epsilon

class ValueIteration:
    def __init__(self):
        pass

    def valueIteration(self, MDP, epsilon = 0.01):


        #AIMA CODE
        '''
         U1 = {s: 0 for s in MDP.states}
        R, T, discount = MDP.R, MDP.T, MDP.discount
        while True:
            U = U1.copy()
            delta = 0
            for s in MDP.states:
                U1[s] = R(s) + discount * max(sum(p * U[s1] for (p, s1) in T(s,a)) for a in MDP.actions(s))
                delta = max(delta, abs(U1[s]-U[s]))
            if delta <= epsilon * (1-discount) / discount:
                return U
        '''


    def maximizePolicy(self, MDP, U):

        pi = {}
        for s in MDP.states:
            pi[s] = max(MDP.actions(s), key=lambda a: self.utility(a, s, U, MDP))
        return pi

    def utility(self, a, s, U, MDP):

        return sum(p * U[s1] for (p, s1) in MDP.T(s, a))
