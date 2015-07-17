from Gene_Types import *
def Transcribe_Brain(starting_layer,neurons):
    """For each neuron in the starting layer,
    find all the neurons that connect to it (have inputs identical to its tag)"""
    i=0
    l=len(starting_layer)
    n=len(neurons)
    temp_layer = []
    for origin_neuron in starting_layer:
        print("Checking origin ",i," of ",l)
        i=i+1
        print("Origin tag is ",origin_neuron.tag)
        j=0
        for neuron in neurons:
            print("neuron: ",j," of ",n)
            j=j+1
            for n_input in neuron.inputs:
                print("input: ",n_input.input)
                if n_input.input==origin_neuron.tag: 
                    temp_layer.append(neuron)
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
