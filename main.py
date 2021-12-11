from TrackImporter import TrackImporter
from Simulator import Simulator
from MDP import MDP
from ValueIteration import ValueIteration

def main():
    ti = TrackImporter("data/test.txt")
    track, start, size, finish = ti.importTrack()

    mdp = MDP(size, track)
    sim = Simulator(track, start, [0, 0], mdp, size, finish, False)

    sim.print_track()
    sim.goSARSA()


    #sim.callValueIteration()

if __name__ == '__main__':
    main()


