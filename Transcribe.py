from Gene_Types import *
class _neuron:
    pass
def Transcribe_Brain(starting_layer,neurons):
    """For each neuron in the starting layer,
    find all the neurons that connect to it (have inputs identical to its tag)"""
    temp_layer = []
    for origin_neuron in starting_layer:
        n=_neuron()
        n.parents=[]
        for neuron in neurons:
            for n_input in neuron.inputs:
                if n_input.input==origin_neuron.tag: 
                    temp_layer.append(neuron)
                    #keeping track of parents would allow for pruning
                    n.parents.append(neuron)
    #return (temp_layer,Transcribe_Brain(temp_layer,neurons))
    return temp_layer

class Organism:
    pass
def Transcribe_Genome(genome):
    o=Organism()
    sensors=[]
    neurons=[]
    for gene in genome:
        t = gene.__class__
        if t==Sensor:
            sensors.append(gene)
        elif t==Neuron:
            neurons.append(gene)
        elif t==Memory:
            neurons.append(gene)
##    brain=Transcribe_Brain(sensors,neurons)
##    o.sensors=sensors
##    o.brain=brain
##    return o
    return sensors,neurons
