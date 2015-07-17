from random import *
class Gene:
   def Init_Gene(self):
      try:
         Gene.items.append(self)
      except AttributeError:
         Gene.items=[self]
   @staticmethod
   def Get_Random():
      return choice(Gene.items)
