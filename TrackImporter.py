
class TrackImporter:
    def __init__(self, file):
        self.file_name = file

    def importTrack(self):
        file = open(self.file_name, 'r')  # opens file
        fileline = file.read().split('\n') #split on line
        startlist = []
        track = []
        fileline = fileline[1:]
        for i in range(len(fileline)):
            row = []
            print(fileline[i])
            if not fileline[i]:
                continue
            for j in range(len(fileline[i])):
                if fileline[i][j] == 'S':
                   startlist.append([i, j])
                   row.append(-1)
                elif fileline[i][j] == '#':
                    row.append(None)
                elif fileline[i][j] == '.':
                    row.append(-1)
                elif fileline[i][j] == 'F':
                    row.append(0)
            track.append(row)
