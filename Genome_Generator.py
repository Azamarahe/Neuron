from Gene import *
class Organism:
    #genome
    #location
    #physical properties
    #neural layers
    pass

def Generate_Genome(size):
    genome=[]
    for i in range(size):
        genome.append(Gene.Get_Random())
    return genome
