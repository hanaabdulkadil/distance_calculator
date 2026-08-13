import math

x1 = float(input("Enter x1:"))
y1 = float(input("Enter y1:"))
x2 = float(input("Enter x2:"))
y2 = float(input("Enter y2:"))
 
distance = math.sqrt(math.pow(x2 - x1 , 2)) + math.pow(y2 - y1 , 2)

print("The distance between the two points is:", distance)
    
    
"""
Using a library is mopre practical than writing all calculations from scratch because it takes less time to code when using functions like sqrt() and pow(). 
The program would be more difficult without sqrt() and pow() because I would have to manually do the code, which would take time and is not practial.
"""