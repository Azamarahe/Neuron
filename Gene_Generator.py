from Gene_Types import *
#Gene Generator
def Generate_Sensors(count):
   """need to generate these first so that other inserting genes have places to insert"""
   for i in range(count):
      Sensor()
def Generate_Genes(count):
   for i in range(count):
      gene_type=Gene_Types.Get_Random()
      gene=gene_type()

def Generation_Sequence(sc,sg):
   Generate_Sensors(sc)
   Generate_Genes(sg)


Generation_Sequence(10,100)
from Genome_Generator import *
g=Generate_Genome(10)
from Transcribe import *
s,n=Transcribe_Genome(g)
#t=Transcribe_Brain(s,n)
