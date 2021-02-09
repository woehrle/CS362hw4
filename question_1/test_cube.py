#Haley Woehrle ONID: 933 345 684
#cs362 HW4, Q1: Calculate Volume of a Cube: Unit testing

import unittest
import cubeVolume

class TestCubeVolume(unittest.TestCase):
  
  def test_cube(self):  #test that the math to cube (x*x*x) calulates properly
    self.assertEqual(cubeVolume.cube(3), 27)  #test that a square of side length of 3 has a volume of 27   
  
  def test_values(self):  #test that value errors are raised if necessary
    self.assertRaises(ValueError, cubeVolume.cube, -8)  #test that an error message appears if side length is negative
  
  def test_types(self):  #test that type errors are raised if necessary
    self.assertRaises(TypeError, cubeVolume.cube, "ty+t7")  #test that an error message appears if input is not number values
  
if __name__ == '__main__':  #run code within conditional
  unittest.main()
    