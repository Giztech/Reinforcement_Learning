
class TrackImporter:
    def __init__(self, file):
        self.file_name = file
        self.start = self.findStartCells()
        self.finish = self.findFinishCells()


    def importTrack(self):
        file = open(self.file_name, 'r')  # opens file
        fileline = file.read().split('\n') #split on line
        startlist = []
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
                    row.append(None)
                elif fileline[i][j] == '.':
                    row.append(-1)
                elif fileline[i][j] == 'F':
                    row.append(0)
            track.append(row)
        return track, startlist, size

    def isWall(self, cell: tuple):
        x = cell[0]
        y = cell[1]
        if self.track[y][x] == '#' or x > len(self.track[0]) or x < 0 or y > len(self.track) or y < 0:
            return True
        else:
            return False

    def findStartCells(self):
        startCells = []
        for y in range(len(self.track)):
            for x in range(len(self.track[0])):
                if self.track[y][x] == 'S':
                    startCells.append((x, y))
        return startCells

    def findFinishCells(self):
        finishCells = []
        for y in range(len(self.track)):
            for x in range(len(self.track[0])):
                if self.track[y][x] == 'F':
                    finishCells.append((x, y))
        return finishCells