from random import *
class Field:
    items=range(100)
    #TODO: consider making scale specific to field
    scale=100
    @staticmethod
    def Get_Random(): return choice(Field.items)
    @staticmethod
    def Get_Range():
        r1=randrange(Field.scale-1)
        r2=randrange(r1+1,Field.scale)
        return (r1,r2)
    def Get_Random_Value(self):
        return randrange(self.scale)
    @staticmethod
    def Get_Random_Value():
        return randrange(Field.scale)
