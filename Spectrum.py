from random import *
class Spectrum:
    items=range(100)
    scale=100
    @staticmethod
    def Get_Random(): return choice(Spectrum.items)
    @staticmethod
    def Get_Range():
        r1=randrange(Spectrum.scale-1)
        r2=randrange(r1+1,Spectrum.scale)
        return (r1,r2)
