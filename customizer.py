from pet import *

class PetCustomizer(Pet):
    def customizer(self, pet):
        self.pet = pet
    def put_on_pants(self):
        pass
    def put_on_shirt(self):
        pass
    def put_on_hat(self):
        pass
    def getFit(self):
        p = False
        s = False
        h = False
        if self.pants == True:
            p = True
        if self.shirt == True:
            s = True
        if self.hat == True:
            h = True
        return p,s,h
class Pants(PetCustomizer):
    def __init__(self,pants):
        self.pants = pants
    def put_on_pants(self):
        return self.pants.put_on_pants()
    
class Shirt(PetCustomizer):
    def __init__(self, Pet):
        PetCustomizer.__init__(Pet)
    def customizer(self):
        self.shirt = True

class Hat(PetCustomizer):
    def __init__(self, Pet):
        PetCustomizer.__init__(Pet)
    def customizer(self):
        self.hat = True
        