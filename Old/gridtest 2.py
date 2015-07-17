import pygame
import time
gridxrange=100
gridyrange=100
void=0
a=0.025
round_digits=3
resolution=0.5
screen_width=600
screen_height=600

minchange=(10**(-round_digits))
minchange=0.5
grid = [[0 for i in range(gridxrange)] for j in range(gridyrange)]
grid[50][50]=100000
def ZeroGrid():
   global grid
   grid = [[0 for i in range(gridxrange)] for j in range(gridyrange)]
def Neighbors(x,y):
  return [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
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
      summ-=4*grid[i][j]
      summ*=a
      #if round(summ,round_digits)==0:
      if abs(summ)<minchange:
         #if i==2 and j==2:
         #   print("sum was ",summ)
         #   print (grid)
         if summ>0:
            pass
            #summ=minchange
         elif summ<0:
            summ=-minchange
      else:
         summ=round(summ,round_digits)
      tempgrid[i][j]=round(grid[i][j]+summ,round_digits)
      if tempgrid[i][j]<resolution:
         tempgrid[i][j]=0
      #if i==30 and j==30:
      #  print("Change = ",summ,grid[i][j],tempgrid[i][j])
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
      val=max(val,0)
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
      #time.sleep(1)   
