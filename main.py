from TrackImporter import TrackImporter
from Simulator import Simulator

def main():
    ti = TrackImporter("data/L-track.txt")
    track = ti.importTrack()

if __name__ == '__main__':
    main()


