from random import *
class List(object):
    @classmethod
    def __init__(cls,self):
        try:
            cls.items.append(self)
        except AttributeError:
            cls.items=[self]
    @classmethod
    def Init_Base(cls,self):
        try:
            cls.items.append(self)
        except AttributeError:
            cls.items=[self]
    @classmethod
    def Get_Random(cls):
        return choice(cls.items)
