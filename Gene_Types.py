from random import *
from Gene import *
from Field import *
from World import *

class Origin(Gene):
   @staticmethod
   def Generate_Tag():
      return len(Origin.items)-1
   def Init_Base(self):
      try:
         Origin.items.append(self)
      except AttributeError:
         Origin.items=[self]
      self.tag=self.Generate_Tag()
      self.Init_Gene()
   @staticmethod
   def Get_Random():
      return choice(items)
class n_input:
         pass
class Sensor(Origin):
   def Value(self,location):
      #TODO: return Field value at location mapped to span range/function
      #requires access to world - use static data in World?
      return World.Get_Field_Value(location,self.field)
   def __init__(self):
      self.field=Field.Get_Random()
      self.range=Field.Get_Range()
      self.Init_Base()
class Neuron(Origin):
   def Set_Inputs(self):
      self.inputs=[]
      for i in range(randrange(2,10)):
         inp=n_input()
         inp.weight=randrange(1,10)
         inp.input=Gene.Get_Random().tag
         self.inputs.append(inp)
   def __init__(self):
      self.Set_Inputs()
      self.Init_Base()
class Memory(Origin):
   def __init__(self):
      self.inputs=[]
      for i in range(randrange(2,10)):
         inp=n_input()
         inp.weight=randrange(-10,10)
         inp.input=Gene.Get_Random().tag
         self.inputs.append(inp)
      self.Init_Base()
class Gene_Types:
   items=(Sensor,Neuron,Memory)
   @staticmethod
   def Get_Random(): return choice(Gene_Types.items)
