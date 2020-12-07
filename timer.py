import time

def timer(sessionTime):
    while sessionTime :
        mins, seconds = divmod(sessionTime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, seconds)
        print(timeformat, end='\r')
        time.sleep(1)
        sessionTime -= 1
def run_timer():    
    sessionTime = input("Enter session time (in minutes): ")
    timer(int(sessionTime))
    breakTime = 1
    totalStudyTime = 0
    tempStudyTime = int(sessionTime)

    for i in range(0, 3) :
        timer(int(sessionTime))
        print("Time for a break..")
        timer(breakTime)
        sessionTime = tempStudyTime
        totalStudyTime += tempStudyTime
        print("Back to studying!")
        i += 1

    totalStudyTime += tempStudyTime
    timer(int(sessionTime))     #calling study timer one last time (4)

    print("Completed study session \n")
    print("Total study time: ", totalStudyTime, "minutes")   


    