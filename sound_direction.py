#get times when detectors detect the sound and return sector of sound direction
def direction(time1,time2,time3):
    times = [time1, time2, time3]
    #find the first detector to detect
    first = times.index(min(times))
    #last detector to detect
    last = times.index(max(times))
    
    #check first which sensor detected and then the last one
    if first == 0:        
        if last == 1:
            return 'sector 1'
        else:
            return 'sector 2'
    elif first == 1:
        if last == 2:
            return 'sector 3'
        else:
            return 'sector 4'   
    else:
        if last == 0:
            return 'sector 5'
        else:
            return 'sector 6'
        

print (direction(24,23,3))
