def convert(num):
    num = num % (24 * 3600)
    hour = num // 3600
    num %= 3600
    minutes = num // 60
    num %= 60
    
    return "%d'hour',%02d'minutes'" % (hour, minutes)