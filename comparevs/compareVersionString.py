def padStringZero(versionstr, length, padding):
    """ Make Version String have same length"""
    return versionstr + [padding] * abs((len(versionstr)-length))

# Method to compare two versions. 
# Return 1 if version2 is smaller, 
# -1 if version1 is smaller,, 
# 0 if equal 

def compareVersion(version1:str, version2:str):
    """Compare two version strings with '.' delimeter """

    # This will split both the versions by '.' 
    version1 = version1.split(".") 
    version2 = version2.split(".")
    
    #checking the difference in the length of the version strings
    checkEqualLength = abs(len(version1)-len(version2))
    
    #padding version string. i.e '1.2' same as '1.2.0'
    if checkEqualLength != 0:

        maxlength = max(len(version1),len(version2))
        
        version1 = padStringZero(version1,maxlength,'0') 
        version2 = padStringZero(version2,maxlength,'0') 
                                           
    for i in range(len(version1)):
        
        # return Version difference if any 
        if int(version1[i]) != int(version2[i]): 
            return int(version1[i]) - int(version2[i])
          
    # Both the versions are equal 
    return 0
  
# Driver method to check the compareVersion function
def compareVersionDriver(version1:str,version2:str)->str:
    
    outcome =  compareVersion(version1, version2) 
    
    if outcome < 0:
        result = f"'{version1}' is smaller than '{version2}'"
        
    elif outcome > 0: 
        result = f"'{version2}' is smaller than '{version1}'"
        
    else:
        result = f"'{version1}' is same version as '{version2}'"
        
    return result

#print(compareVersionDriver("1.1","1.2"))