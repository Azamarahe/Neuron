for ao in accelerating_organisms:
   #move according to verlet
   #save location, add to moved_list
   pass
for mb in moving_attached_bodies:
   #move body, add to moved_list
   pass
for fc in moving_free_cells:
   #move cell, add to moved list
   pass
#detect collisions
#run through moved list
#find possible containing grid(s)
#list inhabitants of grid
#if object is an attached body, check bounding rect
#if object is a free cell, check distance or if is in br of an ab
#add collisions to a collision list
for cc in colliding_cells:
   #assign new velocities to both
   pass
