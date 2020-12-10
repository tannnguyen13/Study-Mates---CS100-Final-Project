import linecache
import os
from pet import *
class File:
    def __init__(self):
        self.nameIndex = 0
        self.totalIndex = 1
        self.numofpets = 2
        self.petname = 3
        self.pettype = 4
        self.petlevel = 5
        self.petexp = 6
        
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

    def update_pet(self, temp):
        with open("user1.txt",'r') as file:
            data = file.readlines()
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