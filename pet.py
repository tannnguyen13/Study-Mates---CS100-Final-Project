# classes for pets: default, mine, cindy's, and tann's
# currently only on terminal, need to figure out how to add visual for each
# also need to discuss more specifics (exp, incrementing exp, clothing for each)
class Pet:
    def __init__(self):
        self.name = "Default"
        self.level = 0
        self.exp = 0
        self.maxLevel = 0;
        self.pants = False
        self.hat = False
        self.shirt = False
    #def setPants(self):
    def customize(self, clothing):
        if clothing == "pants":
            if self.pants == True:
                self.pants = False
            else: 
                self.pants = True
        elif clothing == "shirt":
            if self.shirt == True:
                self.shirt = False
            else: 
                self.shirt = True
        elif clothing == "hat":
            if self.hat == True:
                self.hat = False
            else: 
                self.hat = True
        else:
            print("Oops! The only clothing options are \"pants\", \"shirt\", or \"hat\"")
    def getFit(self):
        if self.pants == True:
            print("pants", end = " ")
        if self.shirt == True:
            print("shirt", end = " ")
        if self.hat == True:
            print("hat", end = " ")
        if self.pants == False and self.shirt == False and self.hat == False:
            print("nothing lol")
    def changeName(self, new_name):
        self.name = new_name
    def getName(self):
        return self.name
    def gainExp(self, expAmount):
        self.exp = self.exp + (expAmount)
    def petIntro(self):
        print("Hello! I am the " + self.name + " study mate. <3 I am a level ", end = "")
        print(self.level, end = "") 
        print("! Nice to meet you <3\nMy exp is: ", end = "")
        print(self.exp)
        print("I am wearing: ", end = "")
        self.getFit()
        print()
    def check_max_level(self):
        if self.level >= self.maxLevel:
            print("Congratulations! I have reached my max level!🙏🏼😇")
            return True
        else:
            return False
class firetype(Pet):
    def __init__(self):
        super().__init__()
        self.name = "Gaby"
        self.level = 1
        self.exp = 0
        self.pants = True
        self.hat = False
        self.shirt = False
        self.maxLevel = 10
    def petIntro(self):
        print("Hello! My name is " + self.name + ". I am a level ", end = "")
        print(self.level, end = "") 
        print(" Fire type! Happy to be here <3\nMy exp is: ", end = "")
        print(self.exp)
        print("I am wearing: ", end = "")
        self.getFit()
        print()
    def gainExp(self, expAmount):
        self.exp = self.exp + (expAmount*2)
    def check_level(self):
        if self.check_max_level() == False:
            i = self.exp
            l = 0
            while i > 0 and self.check_max_level() == False:
                i = i - 100
                l = l+1
            self.level = self.level+(l-1)
            self.exp = i+100 
class watertype(Pet):
    def __init__(self):
        super().__init__()
        self.name = "water"
        self.level = 1
        self.exp = 0
        self.pants = False
        self.hat = True
        self.shirt = False
        self.maxLevel = 8
    def petIntro(self):
        print("Hello! My name is " + self.name + ". I am a level ", end = "")
        print(self.level, end = "") 
        print("! I am a Water type! Study hard! I need more friends <3\nMy exp is: ", end = "")
        print(self.exp)
        print("I am wearing: ", end = "")
        self.getFit()
        print()
    def gainExp(self, expAmount):
        self.exp = self.exp + (expAmount*1.5)
    def check_level(self):
        while self.check_max_level() == False:
            i = self.exp
            l = 0
            while i > 0 and self.check_max_level() == False:
                i = i - 75
                l = l+1
            self.level = self.level+(l-1) 
            self.exp = i+75
            if self.check_max_level() == True:
                self.level = self.maxLevel
class grasstype(Pet):
    def __init__(self):
        super().__init__()
        self.name = "Tann"
        self.level = 1
        self.exp = 0
        self.pants = False
        self.hat = False
        self.shirt = True
        self.maxLevel = 3
    def petIntro(self):
        print("Hello! My name is " + self.name + ". I am a level ", end = "")
        print(self.level, end = "") 
        print("! I am a GRASSTYPE! Excited to join the fun <3\nMy exp is: ", end = "")
        print(self.exp)
        print("I am wearing: ", end = "")
        self.getFit()
        print()
    def gainExp(self, expAmount):
        self.exp = self.exp + (expAmount*1.25)
    def check_level(self):
        if self.check_max_level() == False:
            i = self.exp
            l = 0
            while i > 0:
                i = i - 1
                l = l+1
            self.level = self.level+(l-1)
            self.exp = i+1
            if self.check_max_level() == True:
                self.level = self.maxLevel
#gaby = Pet3()
#gaby.petIntro()
#gaby.changeName("Teehee")
#gaby.gainExp()
def set_type(self, name):
    if (name.lower() == "fire"):
        # Pet.__init__(self, firetype)
        return firetype()
    if (name.lower() == "grass"):
        # Pet.__init__(self, grasstype)
        return grasstype()
    if (name.lower() == "water"):
        # Pet.__init__(self, watertype)
        return watertype()

"""
gaby = Pet3()
gaby.petIntro()
gaby.changeName("Teehee")
gaby.gainExp()
>>>>>>> master
gaby.customize("pants")
gaby.petIntro()
"""