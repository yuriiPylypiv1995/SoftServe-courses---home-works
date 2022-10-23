#Given two ordered pairs calculate the distance between them. Round to two decimal places.

def distance(x1, y1, x2, y2):
    """
    This function calculates the distance between two ordered pairs 
    and round the result to two decimal places.
    
    """
    return round((((x2 - x1)**2 +(y2 - y1)**2)**0.5),2)

print(distance(1, 1, 0, 0))