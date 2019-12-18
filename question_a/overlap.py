def linesOverlap(firstline, secondline):
    return firstline[1] >= secondline[0] and secondline[1] >= firstline[0]
    