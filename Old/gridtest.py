import pygame
import time
gridxrange=60
gridyrange=60
void=0
round_digits=2
screen_width=600
screen_height=600

grid = [[0 for i in range(gridxrange)] for j in range(gridyrange)]
def Neighbors(x,y):
  return [[x-1,y],[x-1,y-1],[x,y-1],[x+1,y-1],[x+1,y],[x+1,y+1],[x,y+1],[x-1,y+1]]
def inxrange(x):
  return (x>-1) and (x<gridxrange)
def inyrange(y):
  return (y>-1) and (y<gridyrange)
def Anneal():
  global grid
  tempgrid=[x[:] for x in grid]
  for i in range(gridxrange):
    for j in range(gridyrange):
      summ=0
      for nx,ny in Neighbors(i,j):
        if inxrange(nx) and inyrange(ny):
          summ+=grid[nx][ny]
        else:
          summ+=void
      tempgrid[i][j]=round(summ/8,round_digits)
      if i==30 and j==30:
        print( tempgrid[i][j])
  grid=[x[:] for x in tempgrid]
  return grid
def draw_grid(screen):
  height=int(screen_height/gridyrange)
  width=int(screen_width/gridxrange)
  #print("height: "+str(height)+" width: "+str(width))
  #print("screen height: "+str(screen_height))
  #print("screen width: "+str(screen_width))
  x=0
  for i in range(gridxrange):
    y=0
    for j in range(gridyrange):
      #print("x="+str(x)+"y="+str(y))
      val=min(grid[i][j],255)
      #if i==30 and j==30:
      #  print (grid[i][j],val)
      screen.fill((val,0,0),(x,y,width,height))
      y+=height
    x+=width
def init():
   pygame.init()
   screen=pygame.display.set_mode((screen_width,screen_height))
   pygame.display.set_caption('Grid Test')
   pygame.mouse.set_visible(0)

   background = pygame.Surface(screen.get_size())
   background = background.convert()
   background.fill((0, 0, 0))

   while(True):
      #screen.blit(background,(0,0))
      screen.fill((0,0,0))
      draw_grid(screen)
      Anneal()
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            return
            #; sys.exit();
      pygame.display.update()
      time.sleep(4)   
