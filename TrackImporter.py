class TrackImporter:
    def __init__(self, file):
        self.file_name = file

    def importTrack(self):
        file = open(self.file_name, 'r')  # opens file
        fileline = file.read().split('\n') #split on line
        startlist = []
        finishlist = []
        track = []
        size = fileline[0]
        fileline = fileline[1:]
        for i in range(len(fileline)):
            row = []
            if not fileline[i]:
                continue
            for j in range(len(fileline[i])):
                if fileline[i][j] == 'S':
                   startlist.append([i, j])
                   row.append(-1)
                elif fileline[i][j] == '#':
                    row.append('#')
                elif fileline[i][j] == '.':
                    row.append(-1)
                elif fileline[i][j] == 'F':
                    finishlist.append([i, j])
                    row.append(0)
            track.append(row)

        return track, startlist, size, finishlist
