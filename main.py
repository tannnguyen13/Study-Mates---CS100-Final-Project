#import pet
#import timer
#from pet import *
#from timer import timer
from timer import *
from menu import menu
from pet import *

if __name__ == "__main__":
    #menu()
    #menu_choice = input("Pick a menu choice \n")
    total = 0
    menu_choice = "1"
    #first = True
    me = Pet()

    while menu_choice != "5":
        menu()
        menu_choice = input("Pick a menu choice \n")

        if menu_choice == "1":
            type = input("Pick your pet type! (Fire🔥), (Water🌊), (Grass🍃) \n")
            
            if type.lower() != ("fire" or "water" or "grass"):
                print("\nInvalid Input! Please pick a type from the list.")
                print("Going back to the main menu\n")
            else:
                me = set_type(me, type)
                
                name = input("What do you want to name your pet? \n")
                me.changeName(name)
                me.petIntro()
                
                time = Timer()
                time.run_timer()
                
                total += time.return_total_time()
                me.gainExp(time.return_total_time())

                me.petIntro()
                me.check_level()

        if menu_choice == "2":
            print("Total minutes studied (lifetime): ")
            print(total, "minutes \n")
        if menu_choice == "3":
            me.petIntro()
        if menu_choice == "5":
            print("Goodbye!")
        elif menu_choice not in ("1" or "2" or "3" or "4" or "5"):
            print("\nInvalid Input! Pick a choice listed in the menu.\n")
