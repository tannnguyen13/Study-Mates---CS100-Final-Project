# classes for pets: default, mine, cindy's, and tann's
# currently only on terminal, need to figure out how to add visual for each
# also need to discuss more specifics (exp, incrementing exp, clothing for each)


class Pet:
    def __init__(self):
        self.name = "Default"
        self.level = 0
        self.exp = 0
        self.maxLevel = 0
        self.pants = False
        self.hat = False
        self.shirt = False
    def changeName(self, new_name):
        self.name = new_name
    def getName(self):
        return self.name
    def gainExp(self, expAmount):
        self.exp = self.exp + (expAmount)
    def petIntro(self, filename = None):
        if filename is None:
            print("Hello! I am the " + self.name + " study mate. <3 I am a level ", end = "")
            print(self.level, end = "") 
            print("! Nice to meet you <3\nMy exp is: ", end = "")
            print(self.exp)
        else:
            petdata = open(filename, 'r')
            print(petdata.readline())
    def check_max_level(self):
        if self.level >= self.maxLevel:
            return True
        else:
            return False


class firetype(Pet):
    def __init__(self):
        super().__init__()
        self.name = "fire"
        self.level = 1
        self.exp = 0
        self.pants = False
        self.hat = False
        self.shirt = False
        self.maxLevel = 5
    def petIntro(self, filename=None): # can call function with or without filename
        if filename is None: # does this if fileName was not passed in
            print("Hello! My name is " + self.name + ". I am a level ", end = "")
            print(self.level, end = "") 
            print(" Fire type! Happy to be here <3\nMy exp is: ", end = "")
            print(self.exp)
        else:
            petdata = open(filename, 'r')
            print(petdata.readline())

    def gainExp(self, expAmount):
        self.exp = self.exp + (expAmount*5)
        self.check_level()
    def check_level(self):
        if self.check_max_level() == False:
            i = self.exp
            l = 0
            while i > 0 and self.check_max_level() == False:
                i = i - 3
                l = l+1
            self.level = self.level+(l-1)
            self.exp = i+3 
            if self.check_max_level() == True:
                self.level = self.maxLevel
class watertype(Pet):
    def __init__(self):
        super().__init__()
        self.name = "water"
        self.level = 1
        self.exp = 0
        self.pants = False
        self.hat = False
        self.shirt = False
        self.maxLevel = 3
    def petIntro(self, filename = None):
        if filename is None:
            print("Hello! My name is " + self.name + ". I am a level ", end = "")
            print(self.level, end = "") 
            print("! I am a Water type! Study hard! I need more friends <3\nMy exp is: ", end = "")
            print(self.exp)
        else:
            petdata = open(filename, 'r')
            print(petdata.readline())
    def gainExp(self, expAmount):
        self.exp = self.exp + (expAmount*2)
        self.check_level()
    def check_level(self):
        while self.check_max_level() == False:
            i = self.exp
            l = 0
            while i > 0 and self.check_max_level() == False:
                i = i - 1
                l = l+1
            self.level = self.level+(l-1) 
            self.exp = i+1
            if self.check_max_level() == True:
                self.level = self.maxLevel
class grasstype(Pet):
    def __init__(self):
        super().__init__()
        self.name = "grass"
        self.level = 1
        self.exp = 0
        self.pants = False
        self.hat = False
        self.shirt = True
        self.maxLevel = 3
    def petIntro(self, filename = None):
        if filename is None:
            print("Hello! My name is " + self.name + ". I am a level ", end = "")
            print(self.level, end = "") 
            print("! I am a GRASSTYPE! Excited to join the fun <3\nMy exp is: ", end = "")
            print(self.exp)
        else:
            petdata = open(filename, 'r')
            print(petdata.readline())
    def gainExp(self, expAmount):
        self.exp = self.exp + (expAmount*1)
        self.check_level()
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

def set_type(self, name):
    if (name.lower() == "fire"):
        return firetype()
    if (name.lower() == "grass"):
        return grasstype()
    if (name.lower() == "water"):
        return watertype()
