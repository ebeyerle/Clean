import unittest
import os, sys
sys.path.append("..")
import generate
import clean

class TestClean(unittest.TestCase):
  def setUp(self):
    self.gener = generate.Generator("folder7")
    self.gener.generate()
    self.cl = clean.MyClean()
    

  def testClean(self):
    self.gener.find_pyc()
    self.cl.find()

    for file in self.cl.pyc:
      if file == "generate.pyc":
        self.cl.pyc.remove(file)

    print len(self.gener.pyc)
    print len(self.cl.pyc)

    self.cl.display()

    self.assertEqual(len(self.gener.pyc), len(self.cl.pyc))

if __name__ == "__main__":
  unittest.main() 
