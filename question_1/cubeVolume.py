#Haley Woehrle ONID: 933 345 684
#cs362 HW4, Q1: Calculate Volume of a Cube

#help writing tests: https://www.youtube.com/watch?v=1Lfv5tUGsn8
import math
    
def cube(x):  #cube function
  if type(x) not in [int, float]:
    raise TypeError("A cube's side length must be a non-negative, real number")
    
  if x < 0:
    raise ValueError("A negative number cannot be a length of a cubed object (today)")

  Volume = float(x) * float(x) * float(x)
  return  Volume
