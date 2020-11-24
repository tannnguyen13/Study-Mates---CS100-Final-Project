class Pet:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.exp = 0

    def changeName(self, new_name):
        self.name = new_name
    def getName(self):
        return self.name
    def gainExp(self):
        self.exp = self.exp + 1
    def petIntro(self):
        print("Hello! I am " + self.name + ". I am a level ", end = "")
        print(self.level, end = "") 
        print(" study mate! Nice to meet you <3")

gaby = Pet("gaby")
gaby.petIntro()