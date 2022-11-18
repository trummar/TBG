#python_fil3.py

from turtle import *

"""
Du finner mye mer på:
https://docs.python.org/3/library/turtle.html
"""

color("red", "red")     # Hva gjør denne? 
begin_fill()            # Her starter området for "farge"

for i in range(4):
    forward(100)
    right(90)

end_fill()              # Her stopper området for "farge"


