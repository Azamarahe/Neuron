class Origin(Gene_Type):
   @staticmethod
   def Generate_Tag():
      return len(Origin.items)-1
   def Init_Base(self):
      try:
         Origin.items.append(self)
      except AttributeError:
         Origin.items=[self]
      self.tag=self.Generate_Tag()
   @staticmethod
   def Get_Random():
      return choice(items)
class Sensor(Origin):
   def __init__(self):
      self.Set_Inputs()
      self.Init_Base()
class Neuron(Origin):
   def __init__(self):
      self.Init_Base()
class Memory(Origin):
   def __init__(self):
      self.Init_Base()
