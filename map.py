#!/usr/bin/python3.5
class room:
  def __init__(self, archetype, Identifier):
    self.maplayout=open(("layouts/"+archetype+str(Identifier)),'r').read()
    
  def printsquaremap(self):
    mapLength=int(math.sqrt(len(self.maplayout)))
    for i in range(0,mapLength):
      print(i*mapLength,i*mapLength+mapLength)
      print(self.maplayout[(i*mapLength):(i*mapLength+mapLength)])

    
