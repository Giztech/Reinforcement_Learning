import itertools

class MDP:
    def __init__(self, size):
        size = size.split(',')
        self.states = list(itertools.product(range(int(size[0])), range(int(size[1]))))
        self.actions = [[-1,-1], [0, -1], [1, -1], [-1, 0], [0, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
        self.prob = .2
        self.rewards = 0
        self.discount = 1 #TUNE <1