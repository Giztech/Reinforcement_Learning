
class ValueIteration:
    def __init__(self):
        pass

    def valueIteration(self, MDP, epsilon=0.01):

        # Copies all states into Utility Function
        Util1 = {s: 0 for s in MDP.statesvi}
        Rewards, Transitions, discount = MDP.Rewards, MDP.Transitions, MDP.discount

        while True:
            # Copies the Utility function each time it loops
            Util = Util1.copy()
            delta = 0
            # Maximizes the Utility while staying with the bounds of epsilon and gamma
            for s in MDP.statesvi:
                for a in MDP.Actions(s):

                    Util1[s] = Rewards(s) + discount * max([sum([p * Util[s1] for (p, s1) in Transitions(s, a)])])
                    delta = max(delta, abs(Util1[s] - Util[s]))

                if delta <= epsilon * (1 - discount) / discount:
                    return Util

    def maximizePolicy(self, MDP, U):
        policy = {}
        for s in MDP.statesvi:
            policy[s] = max(MDP.Actions(s), key=lambda a: self.utilityValue(a, s, U, MDP))
        return policy

    def utilityValue(self, a, s, U, MDP):
        return sum(p * U[s1] for (p, s1) in MDP.Transitions(s, a))


# ((1, 32), (-1, 3))
