def timeConversion(s):
    am_pm = s[-2:]
    time = s[:8]
    hh = int(s[:2])
    mm = int(s[3:5])
    ss = int(s[6:8])
    if am_pm == 'PM' and hh != 12:
        print('{}:{}:{}'.format((hh+12) ,mm ,ss))
    elif am_pm == "AM" and hh ==12:
        print('{}:{}:{}'.format(0,mm ,ss))
    else:
        print('{}:{}:{}'.format(hh ,mm ,ss))

s = '01:05:45PM'
timeConversion(s)
