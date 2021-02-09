#Haley Woehrle ONID: 933 345 684
#cs362 HW4, Q2: Calculate Average from a List of Elements

#help from: https://www.guru99.com/find-average-list-python.html

def calcAverage(x):

  
  if len(x) == 0:  #check if list is empty
    raise Exception("Sorry, list must contain at least one number")
    
  sum_num = 0
  for t in x:
    if type(t) not in [int, float]:  #checks that only numbers are in list
      raise TypeError("Error: Only insert real numbers")  
    sum_num = sum_num + t           

  avg = sum_num / len(x)
  return avg

