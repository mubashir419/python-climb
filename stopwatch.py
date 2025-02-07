import time
def stopwatch():
    print("PRESS ENTER TO START THE STOPWATCH")
    input()
    starttime=time.time()
    print("PRESS ENTER TO STOP THE STOPWATCH")
    input()
    endtime=time.time()
    elapsedtime=endtime-starttime
    print("The elapsed time is:",elapsedtime)
stopwatch()  
