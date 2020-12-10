from fileeditor import *
from pet import Pet
from menu import *

class Abstract_Pet(Pet):                    
    def customizer(self, pet):
        pass
    def get_pants(self):
        pass
    def set_pants(self, type):
        pass
    def get_shirt(self):
        pass
    def get_hat(self):
        pass
    def set_shirt(self, type):
        pass
    def set_hat(self, type):
        pass
    
class Concrete_Pet(Abstract_Pet):
        def customizer(self, Pet):
            return Pet()
        def get_pants(self):
            return "Pants: "
        def set_pants(self):
            return "None"
        def get_shirt(self):
            return "Shirt: "
        def set_shirt(self):
            return "None"
        def get_hat(self):
            return "Hat: "
        def set_hat(self):
            return "None"

class PetDecorator(Pet):                                     #abstarct decorator 
    def __init__(self,decorated_pet):
        self.decorated_pet = decorated_pet
    def get_pants(self):
        return self.decorated_pet.get_pants()
    def get_shirt(self):
        return self.decorated_pet.get_shirt()
    def get_hat(self):
        return self.decorated_pet.get_hat()

class Jeans(PetDecorator):                                  # pants decorator 
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_pants(self):
        return "Jeans 👖"
    def get_pants(self):
       return "Pants: " + self.set_pants() 

class Skirt(PetDecorator):
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_pants(self):
        return "Skirt 👗"
    def get_pants(self):
       return "Pants: " + self.set_pants() 

class Shorts(PetDecorator):
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_pants(self):
        return "Shorts 🩳"
    def get_pants(self):
       return "Pants: " + self.set_pants() 

class TShirt(PetDecorator):
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_shirt(self):
        return "T-Shirt 👚"
    def get_shirt(self):
       return "Shirt: " + self.set_shirt() 

class TankTop(PetDecorator):
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_shirt(self):
        return "Tank Top 🎽"
    def get_shirt(self):
       return "Shirt: " + self.set_shirt() 

class DressShirt(PetDecorator):
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_shirt(self):
        return "Dress Shirt 👔"
    def get_shirt(self):
       return "Shirt: " + self.set_shirt() 

class Beanie(PetDecorator):
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_hat(self):
        return "Beanie 🧢"
    def get_hat(self):
       return "Hat: " + self.set_hat() 

class Crown(PetDecorator):
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_hat(self):
        return "Crown 👑"
    def get_hat(self):
       return "Hat: " + self.set_hat() 

class GradCap(PetDecorator):
    def __init__(self,decorated_pet):
        PetDecorator.__init__(self,decorated_pet)
    def set_hat(self):
        return "Graduation Cap 🎓"
    def get_hat(self):
       return "Hat: " + self.set_hat() 



def main(p, p1, openf):
    change = "1"
    while change != "5":
        CustomMenu()
        change = input()
        if change == "1":               #shirt
            shirtMenu()
            option = input()
            if option == "1":
                p = TShirt(p)
            if option == "2":
                p = TankTop(p)
            if option == "3":
                p = DressShirt(p)
            if option != "1" and option !="2" and option !="3":
                print("\nInvalid Input! Pick a choice listed in the menu.\n")
            print('Fit: ', '\n', p.get_pants(), '\n',  p.get_shirt(), '\n',  p.get_hat())
            openf.updateShirts(p.set_shirt())
            p1.shirt = True

        if change == "2":               #pants
            pantsMenu()
            option = input()
            if option == "1":
                p = Skirt(p)
            if option == "2":
                p = Jeans(p)
            if option == "3":
                p = Shorts(p)
            if option != "1" and option !="2" and option !="3":
                print("\nInvalid Input! Pick a choice listed in the menu.\n")
            print('Fit: ', '\n', p.get_pants(), '\n',  p.get_shirt(), '\n',  p.get_hat())
            openf.updatePants(p.set_pants())
            p1.pants = True
        if change == "3":               #hat
            hatMenu()
            option = input()
            if option == "1":
                p = Beanie(p)
            if option == "2":
                p = Crown(p)
            if option == "3":
                p = GradCap(p)
            if option != "1" and option !="2" and option !="3":
                print("\nInvalid Input! Pick a choice listed in the menu.\n")
            print('Fit: ', '\n', p.get_pants(), '\n',  p.get_shirt(), '\n',  p.get_hat())
            openf.updateHats(p.set_hat())
            p1.hat = True
        if change == '4':
            name = input("What would you like to rename your pet to?")
            p1.changeName(name)
            openf.update_pet(p1)
        if change == "5":
            print("Returning to menu...")
            return p
        if change != "1" and change !="2" and change !="3" and change !="4" and change !="5":
            print("\nInvalid Input! Pick a choice listed in the menu.\n")

if __name__ == "__main__":
    main()
