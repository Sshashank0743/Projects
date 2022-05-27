import time 

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

    print('Time To Go For Sleep!')

t = int(input('Enter time in seconds: '))

countdown(t)
