from datetime import datetime

#get times when detectors detect the sound and return sector of sound direction
def direction(time1,time2,time3):
    times = [datetime.strptime(time1, "%b %d %H:%M:%S %Y"), datetime.strptime(time2, "%b %d %H:%M:%S %Y"), datetime.strptime(time3, "%b %d %H:%M:%S %Y")]
    #find the first detector to detect
    first = times.index(min(times))
    #last detector to detect
    last = times.index(max(times))
    
    #check first which sensor detected and then the last one
    if first == 0:        
        if last == 1:
            return '1'
        else:
            return '2'
    elif first == 1:
        if last == 2:
            return '3'
        else:
            return '4'   
    else:
        if last == 0:
            return '5'
        else:
            return '6'
            
def tempdirection():
    return 1
#test print
#print (direction(24,23,3))
