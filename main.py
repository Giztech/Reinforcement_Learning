from TrackImporter import TrackImporter
from Simulator import Simulator

def main():
    ti = TrackImporter("data/L-track.txt")
    track, start = ti.importTrack()
    sim = Simulator(track, start, [0,0])

if __name__ == '__main__':
    main()


