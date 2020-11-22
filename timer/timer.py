import time

def timer(sessionTime):
    while sessionTime :
        mins, seconds = divmod(sessionTime, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, seconds)
        print(timeformat, end='\r')
        time.sleep(1)
        sessionTime -= 1

sessionTime = input("Input how long you want each study session to be in minutes: ")

breakTime = 5
totalStudyTime = 0
tempStudyTime = int(sessionTime)

for i in range(0, 3) :
    timer(int(sessionTime)*60)
    print("Time for a break..")
    timer(breakTime * 60)
    sessionTime = tempStudyTime
    totalStudyTime += tempStudyTime
    print("Back to studying!")
    i += 1

timer(int(sessionTime))     #calling study timer one last time (4)

print("Completed study session \n")
print("Total study time: ", totalStudyTime, "minutes")
    


