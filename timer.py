import time

class Timer:
    def __init__(self):
        self.totalTime = 0
        self.hours = 0
        self.minutes = 0
        self.sessionTime = 0
    def timer(self,sessionTime):
        while sessionTime :
            mins, seconds = divmod(sessionTime, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, seconds)
            print(timeformat, end='\r')
            time.sleep(1)
            sessionTime -= 1
    def run_timer(self):    
        sessionTime = input("Enter session time (in minutes): ")

        if sessionTime == 0:
            print("Invalid input! You can't study for 0 minutes! \n")
            return None
            
        else:
            breakTime = 1
            totalStudyTime = 0
            tempStudyTime = int(sessionTime)

            for i in range(0, 3) :
                self.timer(int(sessionTime))
                print("Time for a break..")
                self.timer(breakTime)
                sessionTime = tempStudyTime
                totalStudyTime += tempStudyTime
                print("Back to studying!")
                i += 1

            self.timer(int(sessionTime))     #calling study timer one last time (4)
            totalStudyTime += tempStudyTime
            self.totalTime += totalStudyTime

            print("Completed study session \n")
            print("Total study time (for this session): ", totalStudyTime, "minutes")

    def return_total_time(self):
        return self.totalTime

    def print_total_time(self):
        print(self.totalTime)

    def convert_hours(self):
        temp = self.totalTime
        while temp >= 60:
            self.hours += 1
            temp -= 60
        else:
            self.minutes = temp
    
    def return_hours(self):
        return self.hours
    
    def return_minutes(self):
        return self.minutes