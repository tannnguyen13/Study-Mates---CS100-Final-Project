import linecache
import os
from pet import *
class File:
    def __init__(self):
        self.nameIndex = 0
        self.totalIndex = 1
        self.numofpets = 2
        
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
        with open("user1.txt",'r') as file:
            data = file.readlines()
        data[self.numofpets] = str(int(data[self.numofpets]) + 1)+'\n'
        with open("user1.txt",'w') as file:
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
        if checkFile("user1.txt") == True:
            with open("user1.txt",'r') as file:
                data = file.readlines()
            if data[self.numofpets] != "0":
                pet = pet.set_type(data[4])
                pet.changeName(data[3])
                pet.gainExp(data[6])
                pet.level = data[5]
                return pet