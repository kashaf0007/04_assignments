import time 
def countdown(seconds):
    while seconds > 0 :
        mins,secs = divmod(seconds,60)
        time_formate = '{:02d}:{:02d}'.format(mins,secs)
        print(time_formate,end="\r")
        time.sleep(1)
        seconds -= 1
        print("00:00 \n Time's up! ")
        # program
Seconds = int(input("Enter time in seconds :"))
countdown(Seconds)