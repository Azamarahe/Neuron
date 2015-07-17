#gene types = neuron, sensor, neural gland, organ, repro-organ
from random import *


marker_counter=-1
def New_Marker():
   global marker_counter
   marker_counter+=1
   return marker_counter
def Rand_Marker():
   global marker_counter
   return randrange(marker_counter+1)

spectrum_counter=5
def Rand_Spectrum():
   global spectrum_counter
   return randrange(spectrum_counter)


def move(organism,direction,speed):
   Post_Movement(organism,direction,speed)

organ_functions=[move]
def Rand_Organ_Function():
   global organ_functions
   return choice(organ_functions)


class attachment:
   def __init__(self):
      self.marker=Rand_Marker()
      c=0
      while(c==0):
         c=randrange(-10,10)
      self.weight=c
#genes:
####TODO: calculate energy consumption after gene parameters are set, in initialize function,
      ###add mass to genes
      ###genes impart COR
class neuron:
   def __init__(self):
      self.input_markers=[]
      c=randrange(1,10)
      for i in range(c):
         self.input_markers.append(attachment())
      self.input_indices=[] #set by transcription
      self.threshold=None
      self.output_level=None
      self.type="neuron"
      self.value=None
      self.marker=New_Marker()
class sensor:
   def __init__(self):
      self.marker=New_Marker()
      self.spectrum=Rand_Spectrum()
      self.type="sensor"
      self.value=None
class gland:
   def __init__(self):
      self.input_marker=Rand_Marker()
      self._value=0
      self.type="gland"
      self.marker=New_Marker()
class organ:
   def __init__(self):
      self.input_marker=Rand_Marker()
      self.function=Rand_Organ_Function()
      
      
gene_types=[neuron,organ,sensor,gland]


gene_list=[]
#create initial sensors
def Init_Sensors():
   global gene_list
   for i in range(5):
      gene_list.append(sensor())
def Generate_Genes(count):
   global gene_list
   for i in range(count):
      gene_list.append(choice(gene_types)())
def Rand_Organism():
   c=randrange(100)
   for i in range(c):
      pass
