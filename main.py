from TrackImporter import TrackImporter
from Simulator import Simulator
from MDP import MDP
from ValueIteration import ValueIteration

def main():
    ti = TrackImporter("data/L-track.txt")
    track, start, size = ti.importTrack()
    mdp = MDP(size, track)
    sim = Simulator(track, start, [0,0], mdp)

    #sim.callSARSA()

    #sim.print_track()
    sim.callValueIteration()

if __name__ == '__main__':
    main()


