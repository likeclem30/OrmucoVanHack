def check_point_in_bound(line1,line2):  # r and s are ordered pairs
    (x1,x2) = line1
    line2 = (y1,y2) = line2
    
    #print("\n xb3=",max(y1,y2))
    #print("\n type(y1)=",type(y1))
    return (min(line2) <= x1 <= max(line2)) or (min(line2) <= x2 <= max(line2))
    
#check_point_in_bound(firstline,secondline)
def check_overlap(line1,line2):
    return check_point_in_bound(firstline,secondline) or check_point_in_bound(secondline,firstline)
#print("\n overlap :",check_overlap(firstline,secondline))

def linesOverlapDriver(firstline,secondline):
    result = check_overlap(firstline, secondline)
    if result is True:
        result = f"line '{firstline}' and '{secondline}' Overlap"
    else:
        result = f"line '{firstline}' and '{secondline}' do not Overlap"
    return result
firstline = (1,5)
secondline = (2,6) #linesOverlap(1,5,6,2) should overlap. i.e order lines
print(linesOverlapDriver(firstline,secondline))