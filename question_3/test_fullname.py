import unittest
import fullname

class TestName(unittest.TestCase):
  
  def test_name(self):  #test that the first and last name combine with a space between
    self.assertEqual(fullname.buildName('Haley', 'Woehrle'), 'Haley Woehrle')  #test function builds full name
    #self.assertEqual(fullname.buildName('Hal', 'Woe '), 'HalWoe ')  #fail test

  def test_full(self):  #test to see if the list is empty
    self.assertIsNotNone(fullname.buildName('Harry', 'Potter'), msg = "Input is not none")  #test there are elements
    #self.assertIsNotNone(fullname.buildName('', 'Pots'), msg = "Input is none") #fail test
  
  def test_types(self):  #test that type errors are raised if necessary
    self.assertRaises(TypeError, fullname.buildName, "ty+t7")  #test that non number types recieve error message
    #self.assertRaises(TypeError, fullname.buildName, "22") #fail test
  
if __name__ == '__main__':  #run code within conditional
  unittest.main()