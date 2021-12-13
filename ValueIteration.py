class ValueIteration:
    def __init__(self):
        pass

    def valueIteration(self, MDP, epsilon=0.01):
        """
        Value Iteration Algorithm that replicates the Bellman Equation by maximizing both sides of the Utility Function
        """


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
        """
        Given the MDP and the Utility Function find an optimal policy
        """
        policy = {}
        # print(U)
        for s in MDP.statesvi:

            policy[s] = max([MDP.Actions(s)], key=lambda a: sum([p * U[s1] for (p, s1) in MDP.Transitions(s, a)]))
        return policy

# ((1, 32), (-1, 3))