def convert(num):
    
    hour = num // 60
    minutes = num * 60 % 24 
    
    return("%d hours, %02d minutes" % (hour, minutes))
