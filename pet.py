# classes for pets: default, mine, cindy's, and tann's
# currently only on terminal, need to figure out how to add visual for each
# also need to discuss more specifics (exp, incrementing exp, clothing for each)
class Pet:
    def __init__(self):
        self.name = "Default"
        self.level = 0
        self.exp = 0
        self.pants = False
        self.hat = False
        self.shirt = False
    def setPants(self):
        if self.pants == True:
            self.pants = False
        else: 
            self.pants = True
    def setShirt(self):
        if self.shirt == True:
            self.shirt = False
        else: 
            self.shirt = True
    def setHat(self):
        if self.hat == True:
            self.hat = False
        else: 
            self.hat = True
    def changeName(self, new_name):
        self.name = new_name
    def getName(self):
        return self.name
    def gainExp(self):
        self.exp = self.exp + 1
    def petIntro(self):
        print("Hello! I am the " + self.name + " study mate. :( I am a level ", end = "")
        print(self.level, end = "") 
        print("! Nice to meet you <3\nMy exp is: ", end = "")
        print(self.exp)

class Pet1(Pet):
    def __init__(self):
        self.name = "Gaby"
        self.level = 1
        self.exp = 10
        self.pants = True
        self.hat = False
        self.shirt = False
    def petIntro(self):
        print("Hello! My name is " + self.name + ". I am a level ", end = "")
        print(self.level, end = "") 
        print("! Happy to be here <3\nMy exp is: ", end = "")
        print(self.exp)

class Pet2(Pet):
    def __init__(self):
        self.name = "Cindy"
        self.level = 3
        self.exp = 55
        self.pants = False
        self.hat = True
        self.shirt = False
    def petIntro(self):
        print("Hello! My name is " + self.name + ". I am a level ", end = "")
        print(self.level, end = "") 
        print("! Study hard! I need more friends <3\nMy exp is: ", end = "")
        print(self.exp)

class Pet3(Pet):
    def __init__(self):
        self.name = "Tann"
        self.level = 4
        self.exp = 99
        self.pants = False
        self.hat = False
        self.shirt = True
    def petIntro(self):
        print("Hello! My name is " + self.name + ". I am a level ", end = "")
        print(self.level, end = "") 
        print("! Excited to join the fun <3\nMy exp is: ", end = "")
        print(self.exp)
        print("I am wearing: ", end = "")
        if self.pants == True:
            print("pants!")
        if self.shirt == True:
            print("a shirt!")
        if self.hat == True:
            print("a hat!")
        if self.pants == False and self.shirt == False and self.hat == False:
            print("nothing lol")

gaby = Pet3()
gaby.petIntro()
gaby.changeName("Teehee")
gaby.gainExp()
gaby.petIntro()
