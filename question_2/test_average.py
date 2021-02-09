import unittest
import average

class TestListAvg(unittest.TestCase):
  
  def test_avg(self):  #test that the math to average the sum is correct
    self.assertEqual(average.calcAverage([1, 2, 3, 4, 5]), 3)  #test that the sum of 1-5 is 3
  
  def test_empty(self):  #test to see if the list is empty
    self.assertIsNone(None)  #test if there are elements in the list 
  
  def test_types(self):  #test that type errors are raised if necessary
    self.assertRaises(TypeError, average.calcAverage, "ty+t7")  #test that non number types recieve error message
  
if __name__ == '__main__':  #run code within conditional
  unittest.main()