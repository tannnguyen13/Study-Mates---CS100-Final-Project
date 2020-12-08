#import pet
#import timer
#from pet import *
#from timer import timer
from timer import *
from menu import menu
from pet import *

if __name__ == "__main__":
    menu()
    menu_choice = input("Pick a menu choice \n")
    total = 0

    while menu_choice != "5":
        if menu_choice == "1":
            type = input("Pick your pet type! (Fire🔥), (Water🌊), (Grass🍃) \n")

            me = Pet()
            me = set_type(me, type)
            
            name = input("What do you want to name your pet? \n")
            me.changeName(name)
            me.petIntro()
            
            time = Timer()
            time.run_timer()
            
            total += time.return_total_time()

        if menu_choice == "2":
            print("Total minutes studied (lifetime): ")
            print(total, "minutes \n")
        if menu_choice == "5":
            print("Goodbye!\n")
        menu()
        menu_choice = input("Pick a menu choice \n")

    
    

#timer(0)
