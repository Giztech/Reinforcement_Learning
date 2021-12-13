from TrackImporter import TrackImporter
from Simulator import Simulator
from MDP import MDP
from ValueIteration import ValueIteration

def main():
    ti = TrackImporter("data/L-track.txt")
    track, start, size, finish = ti.importTrack()

    mdp = MDP(size, track, start)
    sim = Simulator(track, start, mdp, size, False)

    #im.print_track()
    #sim.goSARSA()


    sim.callValueIteration()

if __name__ == '__main__':
    main()