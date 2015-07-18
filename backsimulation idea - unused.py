class Organ:
   def Simulate(self):
      if self.Value()>self.threshold:
         self.Activate()
   def Value(self):
      total=0
      for inp in self.inputs:
         total+=inp.Value()
      return total

def Simulate(organism):
   for sensor in orgaism.sensors:
      sensor.Localize((organism.x,organism.y))
   for i in range(len(organism.memories)):
      organism.memory[i].set(organism.mem_val[i])
   for organ in organism.organs:
      organ.Simulate()
   for sensor in orgaism.sensors:
      sensor.Localize((None,None))
