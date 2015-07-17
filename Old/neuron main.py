#CONSTANTS:
genetypesensor=10
geneteypeneuron=20
genetypeorgan=30
class Gene:
    def __init__(self,genetype):
        self.type=genetype


class Creature:
    def Transcribe():
        Sort_Genes()
        Wire_Brain()
        Wire_Organs()
    def Sort_Genes():
        self.sensors=[]
        self.neurons = []
        self.organs = []
        for gene in self.genome:
            if gene.type = genetypesensor:
                self.sensors.append(gene)
            elif gene.type = genetypeneuron
                self.neurons.append(gene)
            elif gene.type = genetypeorgan
                self.organs.append(gene)
    def Wire_Brain():
        self.brain=[]
        Connect_Layer(self.sensors)
    def Connect_Layer(starting_layer):
        temp_layer = []
        for input_neuron in starting_layer:
            for neuron in self.neurons:
                for inp in neuron.inputs:
                        if inp.name==input_neuron.name: 
                            #build new layer
                            temp_layer.append(neuron)
                            #mark neuron as more connected
                            inp.set=true
                            #connect input neuron to layer neuron
                            input_neuron.outputs.append(neuron)
                #remove neuron from list if fully connected
                unset_inputs=False
                for inp in neuron.inputs:
                    if inp.set==False: 
                        unset_inputs=true
                        exit
                if not unset_inputs: neurons.remove(neuron)
        if len(temp_layer)>0:
            #move neurons in the last layer forward if they depend on a neuron in the current layer, and remove redundancy:
            #TODO: loop through all earlier levels for duplicates
            for neuron1 in starting_layer:
                for neuron2 in temp_layer:
                    if neuron1==neuron2: starting_layer.remove(neuron1)
            self.brain.append(list(temp_layer))
            if len(self.brain)<MAX_BRAIN_SIZE:
                Connect_Layer(self.brain[-1])
    def Wire_Organs():
        for organ in self.organs:
            for neuron in self.brain[-1]:
                for inp in organ.inputs:
                    if inp==neuron.name:
                        neuron.outputs.append(organ)
    def Simulate():
        Read_Sensors()
        Simulate_Brain()
        Simulate_Organs()
    def Read_Sensors():
        #each sensor reads from the grid location according to its spectrum
        #then sends result to outputs
        for sensor in self.sensors:
            for output in sensor.outputs:
                output.take(Grid[self.x,self.y].properties[sensor.property])
    def Simulate_Brain():
        retry=[]
        for layer in brain:
            for neuron in layer:
                if neuron.ready:
                    neuron.simulate #calculates and stimulates outputs
                else:
                    retry.append(neuron)
            for neuron in retry:
                if neuron.ready:
                    neuron.simulate
                    retry.remove(neuron)
        #loop through each layer,
        #signal each neuron to respond to its inputs and signal its outputs
        #if a neuron can't function yet (returns false), add it to the next loop
        #stop if max iterations reached
def Simulate():
  for creature in creatures:
    creature.Simulate()
  
    #simulate all creatures
        #reproductive organs need to generate new genome,
        #which includes mutation
    #simulate physics

        #tasks: propogate forces,
        #calculate normals & friction,
        #evaluate movements
        #evaluate reactions (not sure of placement)
        #evaluate propogation of effects & properties
    
    
#neuron has 'take' in order to collect inputs
#'ready' when all inputs are collected... possibly a function
#more limited organ names could help make sure organs are usually connected
