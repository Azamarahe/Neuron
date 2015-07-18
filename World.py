from Field import *
class World:
   @staticmethod
   def Init(width,height):
      World.width=width
      World.height=height
      World.field_value=[[None for location in range(width*height) ] for field in Field.items]
   @staticmethod
   def Generate_Random_Fields():
      for field in Field.items:
         for x in range(World.width):
            for y in range(World.height):
               World.field_value[field][x+y*World.width]=Field.Get_Random_Value()
   @staticmethod
   def Get_Field_Value(location,field):
      return World.field_value[field][location[0]+location[1]*World.width]
