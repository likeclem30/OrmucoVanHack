def linesOverlap(firstline, secondline):
    return firstline[1] >= secondline[0] and secondline[1] >= firstline[0]

def linesOverlapDriver(firstline,secondline):
    result = linesOverlap(firstline, secondline)
    if result is True:
        result = f"line '{firstline}' and '{secondline}' Overlap"
    else:
        result = f"line '{firstline}' and '{secondline}' do not Overlap"
    return result

firstline = (1,5)
secondline = (2,6)
print(linesOverlap(firstline,secondline))  