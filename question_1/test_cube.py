#Haley Woehrle ONID: 933 345 684
#cs362 HW4, Q1: Calculate Volume of a Cube: Unit testing

import unittest
import cubeVolume

class TestCubeVolume(unittest.TestCase):
  
  def test_cube(self):  #test that the math to cube (x*x*x) calulates properly
    #self.assertEqual(cubeVolume.cube(3), 9)  #fail test case
    self.assertEqual(cubeVolume.cube(3), 27)  #pass test  
  
  def test_values(self):  #test that value errors are raised if necessary
    self.assertRaises(ValueError, cubeVolume.cube, -8)  #pass test 
    #self.assertRaises(ValueError, cubeVolume.cube, 8)  #fail test case
  
  def test_types(self):  #test that type errors are raised if necessary
    self.assertRaises(TypeError, cubeVolume.cube, "ty+t7")  #pass test 
    #self.assertRaises(TypeError, cubeVolume.cube, "143")  #fail test case
  
if __name__ == '__main__':  #run code within conditional
  unittest.main()
    