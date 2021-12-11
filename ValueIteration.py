
class ValueIteration:
    def __init__(self):
        pass


    def valueIteration(self, MDP, epsilon=0.01):

        # Copies all states into Utility Function
        Util1 = {s: 0 for s in MDP.states}
        Rewards, Transitions, discount = MDP.Rewards, MDP.Transitions, MDP.discount

        while True:
            # Copies the Utility function each time it loops
            Util = Util1.copy()
            delta = 0
            # Maximizes the Utility while staying with the bounds of epsilon and gamma
            for s in MDP.states:
                Util1[s] = Rewards(s) + discount * max(
                    sum(p * Util[s1] for (p, s1) in Transitions(s, a)) for a in MDP.actions(s))
                delta = max(delta, abs(Util1[s] - Util[s]))
            if delta <= epsilon * (1 - discount) / discount:
                return Util

    def maximizePolicy(self, MDP, U):
        policy = {}
        for s in MDP.states:
            policy[s] = max(MDP.actions(s), key=lambda a: sum(p * U[s1] for (p, s1) in MDP.Transitions(s, a)))
        return policy


