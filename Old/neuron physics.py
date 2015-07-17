#clumping physics
#accelerations
for particle in force_queue:
   #force = apply traction, terrain, friction effects
   #apply velocity...worry about detachment in velocity step
   particle.velocity=2D_Add(particle.velocity,2D_Div(force,mass))
#projection, collision detection
for particle in vel_queue:
   collisions = Project(particle) #also applies new velocities to particles
   Process(collisions)

def Process(collisions):
   collision_queue+=collisions
   for collision in collisions:
      Collide(collision.p1,collision.p2) #assigns velocities
   Process_Detachments()

def Process_Detachments():
   for collision in collision_queue:
      for particle in [collision.p1,collision.p2]:
         for neighbor in particle.neighbors:
            if Difference(particle.velocity,neighbor.particle.velocity)>neighbor.strength:
               particle.neighbors.remove(neighbor)
               collision_queue.append(
