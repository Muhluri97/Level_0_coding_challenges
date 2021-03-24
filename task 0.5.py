def area(a,b,c):
    semi_parameter = (a+b+c)/2
    area = (semi_parameter*(semi_parameter-a)*(semi_parameter-b)*(semi_parameter-c)) ** 0.5
    return area
    
