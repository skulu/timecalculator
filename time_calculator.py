def add_time(start, duration, start_day=0):
    days = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 0
    }

    # Getting start time
    start = start.split(':')
    tmp = start[1]
    start.pop()
    start.extend(tmp.split())
    start[0] = int(start[0])
    start[1] = int(start[1])
    
    if start[-1] =='PM':
        start[0] += 12
    
    # Getting duration
    duration = duration.split(':')
    duration = [int(a) for a in duration]
    
    # Calculate new time [hours, minutes, days later, AM/PM]
    new = []
    new.append(start[0] + duration[0])
    new.append(start[1] + duration[1])
    new[0] += new[1]//60
    new[1] = new[1]%60
    new.append(new[0]//24)
    new[0] = new[0]%24

    if new[0] >= 12:
        new.append('PM')
        new[0] -= 12
    else:
        new.append('AM')

    if new[0] == 0:
        new[0] = 12
    
    # Formatting the return string
    # Time
    if len(str(new[1])) == 1:
        minute = '0' + str(new[1])
    else:
        minute = str(new[1])
    new_time = str(new[0]) + ':' + minute + ' ' + str(new[3])

    # Day of week
    if start_day != 0:
        start_day = start_day.title()
        new_day = (new[2] + days[start_day])%7
        new_day = list(days.keys())[list(days.values()).index(new_day)]
        new_time += (', ' + str(new_day))
    
    # Days later
    if new[2] == 1:
        new_time += ' (next day)'
    elif new[2] > 1:
        new_time += (f' ({str(new[2])} days later)')
        
        
    return new_time
