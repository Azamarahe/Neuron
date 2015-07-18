#forward propogation:
def Simulate():
   for sensor in sensors:
      sensor.value=sensor.Value((x,y))
   for layer in brain:
      for neuron in layer:
         #can make the following a function, if any input
         #isn't set, use a copy of the brain, and add the neuron to the end
         #of the next layer -
         #however, if I make sure layers are added to the brain only when
         #all inputs are in lower layers, then this isn't needed.
         total=0
         for inp in neuron.inputs:
            total+=inp.input.value*inp.weight
         if total>neuron.neuron_abstract.threshold:
            neuron.value=neuron.output

         
