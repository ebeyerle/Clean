import os, sys

class MyClean(object):

  def __init__(self):
    self.pyc = []

  def find(self):
    for root, dirs, files in os.walk(os.getcwd()):
      for file in files:
        if file.endswith(".pyc"):
          self.pyc.append(file)
          os.remove(os.path.join(root, file))

  def display(self):
    print "Cleaning..."
    print "The following files have been removed..."
    if len(self.pyc) == 0:
      print "There are no .pyc files to remove..."
    else:
      for file in self.pyc:
        print file
    

if __name__ == "__main__":

  cleaner = MyClean()
  cleaner.find()
  cleaner.display()
