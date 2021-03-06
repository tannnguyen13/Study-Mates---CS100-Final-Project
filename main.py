#import pet
#import timer
#from pet import *
#from timer import timer
from fileeditor import *
from timer import *
from customizer import *
from menu import *
import subprocess
from pet import *
#from customizer import *

if __name__ == "__main__":
    Welcome()
    openf = File()
    if openf.checkFile("user1.txt") == True:
        # user1 = open("user1.txt","a")
        total = 0
        menu_choice = "1"
        p = Concrete_Pet()
        me = Pet()
        name = input(" Enter your name: ")
        openf.addName(name)
    else:
        menu_choice = "1"
        p = Concrete_Pet()
        p = openf.get_customizer()
        if openf.check_pet() != False:
            me = openf.get_pet()
        else:
            me = Pet()
        total = openf.get_total()
        
    
    while menu_choice != "5":
        menu()
        menu_choice = input("Pick a menu choice \n")

        if menu_choice == "1":
            if openf.check_pet() == False:
                type = input("Pick your pet type! (Fire🔥), (Water🌊), (Grass🍃) \n")
                if type.lower() == "water" or type.lower() == "fire" or type.lower() == "grass":
                    me = set_type(me, type)
                    
                    name = input("What do you want to name your pet? \n")
                    me.changeName(name)
                    me.petIntro()
                    
                    time = Timer()
                    time.run_timer()
                    
                    total += time.return_total_time()
                    openf.update_total(time.return_total_time())
                    me.gainExp(time.return_total_time())

                    openf.addPet(me, type)
                    
                    me.petIntro()
                    if me.check_max_level() == True:
                        print("Congratulations! I have reached my max level! 😇🙏🏼")
                else:
                    print("\nInvalid Input! Please pick a type from the list.")
                    print("Going back to the main menu...\n")

                '''
                if (type.lower() != "water") or (type.lower() != "fire") or (type.lower() != "grass"):
                    print("\nInvalid Input! Please pick a type from the list.")
                    print("Going back to the main menu...\n")
                else:
                    me = set_type(me, type)
                    
                    name = input("What do you want to name your pet? \n")
                    me.changeName(name)
                    me.petIntro()
                    
                    time = Timer()
                    time.run_timer()
                    
                    total += time.return_total_time()
                    openf.update_total(time.return_total_time())
                    me.gainExp(time.return_total_time())

                    openf.addPet(me, type)
                    
                    me.petIntro()
                    if me.check_max_level() == True:
                        print("Congratulations! I have reached my max level! 😇🙏🏼")
                    '''
            else:
                    time = Timer()
                    time.run_timer()
                    total += time.return_total_time()
                    openf.update_total(time.return_total_time())
                    me.gainExp(time.return_total_time())
                    # updates the pet in the txt file
                    openf.update_pet(me)

        if menu_choice == "2":
            print("Total minutes studied (lifetime): ")
            print(total, "minutes \n")
        if menu_choice == "3":
            me.petIntro()
            print('Fit: ', '\n', p.get_pants(), '\n',  p.get_shirt(), '\n',  p.get_hat())
        if menu_choice == "4":
            p = main(p, me, openf)
        if menu_choice == "5":
            print("Goodbye!")
        if menu_choice != "1" and menu_choice !="2" and menu_choice !="3" and menu_choice !="4" and menu_choice !="5":
            print("\nInvalid Input! Pick a choice listed in the menu.\n")