#import pet
#import timer
#from pet import *
#from timer import timer
from timer import timer, run_timer
from menu import menu
from pet import *

if __name__ == "__main__":
    menu()
    type = input("Pick your pet type! (Fire🔥), (Water🌊), (Grass🍃) \n")

    me = Pet()
    me = set_type(me, type)
    
    name = input("What do you want to name your pet? \n")
    me.changeName(name)
    me.petIntro()
    
    run_timer()
    choice = input("Do you want to continue studying? ")
    while (choice == "yes") or (choice == "Yes") or (choice == "YES"):
        run_timer()
        choice = input("Do you want to continue studying? ")
        if (choice == "no") or (choice == "No") or (choice == "NO"):
            print("Goodbye!")
    
    

#timer(0)
