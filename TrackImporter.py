class TrackImporter:
    def __init__(self, file):
        self.file_name = file

    def importTrack(self):
        """Kieran Ringel
        Reads in file and creates a 2D array for the track"""
        file = open(self.file_name, 'r')  # opens file
        fileline = file.read().split('\n') #split on line
        startlist = []
        finishlist = []
        track = []
        size = fileline[0]
        fileline = fileline[1:]
        for i in range(len(fileline)):  #iterate over lines
            row = []
            if not fileline[i]:
                continue
            for j in range(len(fileline[i])):   #iterate over characters in line
                if fileline[i][j] == 'S':
                   startlist.append([i, j])     #create list of finishing positions
                   row.append(-1)
                elif fileline[i][j] == '#':
                    row.append('#')
                elif fileline[i][j] == '.':
                    row.append(-1)
                elif fileline[i][j] == 'F':
                    finishlist.append([i, j])   #create list of starting positions
                    row.append(0)
            track.append(row)

        return track, startlist, size, finishlist
