from TrackImporter import TrackImporter
from Simulator import Simulator
from MDP import MDP
from ValueIteration import ValueIteration

def main():
    ti = TrackImporter("data/L-track.txt")
    track, start, finish ,size = ti.importTrack()

    mdp = MDP(size, track)
    sim = Simulator(track, start, finish, [0, 0], mdp, size, False)

    #sim.goSARSA()

    #sim.print_track()
    sim.callValueIteration()

if __name__ == '__main__':
    main()


