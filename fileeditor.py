import linecache
import os
from pet import *
from customizer import *
class File:
    def __init__(self):
        self.nameIndex = 0
        self.totalIndex = 1
        self.numofpets = 2
        self.petname = 3
        self.pettype = 4
        self.petlevel = 5
        self.petexp = 6
        self.shirt = 7
        self.pants = 8
        self.hat = 9
        
    def checkFile(self, name):
        return os.stat(name).st_size == 0

    def addName(self, name):
        user1 = open("user1.txt","a")
        user1.write(str(name)+'\n')
        user1.write("0\n")
        user1.write("0\n")
        user1.close()

    def addPet(self, pet, pettype):
        user1 = open("user1.txt", 'a')
        user1.write(pet.name +'\n')
        user1.write(pettype.lower()+'\n')
        user1.write(str(pet.level)+'\n')
        user1.write(str(pet.exp)+'\n')
        user1.write('\n')
        user1.write('\n')
        user1.write('\n')
        with open("user1.txt",'r') as file:
            data = file.readlines()
        data[self.numofpets] = str(int(data[self.numofpets]) + 1)+'\n'
        with open("user1.txt",'w') as file:
            file.writelines(data)

    def update_pet(self, temp):
        with open("user1.txt",'r') as file:
            data = file.readlines()
        data[self.petname] = (str(temp.name)+'\n')
        data[self.petlevel] = (str(temp.level)+'\n')
        data[self.petexp] = (str(temp.exp)+'\n')
        with open("user1.txt", 'w') as file:
            file.writelines(data)

    def update_total(self, total):
        with open("user1.txt",'r') as file:
            data = file.readlines()
        data[self.totalIndex] = str(int(data[self.totalIndex]) + total)+'\n'
        with open("user1.txt",'w') as file:
            file.writelines(data)

    def get_total(self):
        with open("user1.txt",'r') as file:
            data = file.readlines()
        return int(data[self.totalIndex])

    def get_pet(self):
        pet = Pet()
        if self.checkFile("user1.txt") == False:
            with open("user1.txt",'r') as file:
                data = file.readlines()
            if data[self.numofpets] != "0":
                pet = set_type(pet, (str(data[4]).rstrip('\n')))
                pet.changeName(data[3].rstrip('\n'))
                pet.exp = (int(data[6]))
                pet.level = int(data[5])
                return pet

    def check_pet(self):
        with open("user1.txt",'r') as file:
                data = file.readlines()
        if data[self.numofpets] != "0\n":
            return True
        else:
            return False

    def updateShirts(self, shirt):
        with open("user1.txt",'r') as file:
                data = file.readlines()
        data[self.shirt] = shirt[:len(shirt) - 2] + '\n'
        with open("user1.txt", 'w') as file:
            file.writelines(data)

    def updatePants(self, pants):
        with open("user1.txt",'r') as file:
                data = file.readlines()
        data[self.pants] = pants[:len(pants) - 2] + '\n'
        with open("user1.txt", 'w') as file:
            file.writelines(data)

    def updateHats(self, hat):
        with open("user1.txt",'r') as file:
                data = file.readlines()
        data[self.hat] = hat[:len(hat) - 2] + '\n'
        with open("user1.txt", 'w') as file:
            file.writelines(data)

    def get_customizer(self):
        p = Concrete_Pet()
        with open("user1.txt",'r') as file:
            data = file.readlines()
        # block for getting the shirts
        if(data[self.shirt] == "T-Shirt\n") :
            p = TShirt(p)
        if(data[self.shirt] == "Tank Top\n") :
            p = TankTop(p)
        if(data[self.shirt] == "Dress Shirt\n") :
            p = DressShirt(p)
        # block for getting the pants
        if(data[self.pants] == "Jeans\n" ):
            p = Jeans(p)
        if(data[self.pants] == "Skirt\n"):
            p = Skirt(p)
        if(data[self.pants] == "Shorts\n"):
            p = Shorts(p)
        # block for getting the hats
        if(data[self.hat] == "Graduation Cap\n"):
            p = GradCap(p)
        if(data[self.hat] == "Crown\n"):
            p = Crown(p)
        if(data[self.hat] == "Beanie\n"):
            p = Beanie(p)
        return p