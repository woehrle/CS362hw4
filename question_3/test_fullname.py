import unittest
import fullname

class TestName(unittest.TestCase):
  
  def test_name(self):  #test that the first and last name combine with a space between
    self.assertEqual(fullname.buildName('Haley', 'Woehrle'), 'Haley Woehrle')  #test function builds full name

  def test_full(self):  #test to see if the list is empty
    self.assertIsNotNone(fullname.buildName('Harry', 'Potter'), msg = "Input is not none")  #test there are elements
  
  def test_types(self):  #test that type errors are raised if necessary
    self.assertRaises(TypeError, fullname.buildName, "ty+t7")  #test that non number types recieve error message
  
if __name__ == '__main__':  #run code within conditional
  unittest.main()