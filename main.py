from TrackImporter import TrackImporter
from Simulator import Simulator
from MDP import MDP
from ValueIteration import ValueIteration

def main():
    ti = TrackImporter("data/R-track.txt")
    track, start, size, finish = ti.importTrack()

    mdp = MDP(size, track, start)
    sim = Simulator(track, start, [0, 0], mdp, size, True) #False - restart last location, True - restart beginning

    # sim.print_track()
    sim.goSARSA()


    #sim.callValueIteration()

if __name__ == '__main__':
    main()


