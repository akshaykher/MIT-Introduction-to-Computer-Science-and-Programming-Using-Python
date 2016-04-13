#importing math module for using the function tan and variable pi
import math

def polysum(n,s):
    """
    Write a function called polysum that takes 2 arguments, n and s. 
    This function should sum the area and square of the perimeter of the regular polygon. 
    The function returns the sum, rounded to 4 decimal places.
    """
    #The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    area = (0.25*n*s**2)/(math.tan((math.pi)/n))
    #The perimeter of a polygon is: length of the boundary of the polygon
    perimeter = n*s
    
    #calculating sum
    sum = area + perimeter**2
    #rounding sum to 4 decimal places
    sum = round(sum,4)
    #returning sum
    return(sum)
    