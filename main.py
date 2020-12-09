#import pet
#import timer
#from pet import *
#from timer import timer
from timer import *
from menu import *
import subprocess
from pet import *
#from customizer import *

if __name__ == "__main__":
    Welcome()
    user = open("user1.txt","r")
    if user.readline() != "":
        user1 = open("user1.txt","a")
        total = 0
        menu_choice = "1"
        me = Pet()
        name = input(" Enter your username: ")
        passw = input(" Enter your password: ")
        user1.write(str(name)+'\n')
        user1.write(str(passw)+'\n')
    
    while menu_choice != "5":
        menu()
        menu_choice = input("Pick a menu choice \n")

        if menu_choice == "1":
            type = input("Pick your pet type! (Fire🔥), (Water🌊), (Grass🍃) \n")
            
            if type.lower() != ("fire" or "water" or "grass"):
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
                me.gainExp(time.return_total_time())

                user1.write(name.lower()+'\n')
                user1.write(type.lower()+'\n')
                
                me.petIntro()
                if me.check_max_level() == True:
                    print("Congratulations! I have reached my max level! 😇🙏🏼")

                user1.write(str(me.level)+'\n')
                user1.write(str(me.exp)+'\n')
        if menu_choice == "2":
            print("Total minutes studied (lifetime): ")
            print(total, "minutes \n")
        if menu_choice == "3":
            me.petIntro(filename="user1.txt")
            print("to be implemented")
        if menu_choice == "4":
            import customizer
            customizer.main()
        if menu_choice == "5":
            print("Goodbye!")
        if menu_choice != "1" and menu_choice !="2" and menu_choice !="3" and menu_choice !="4" and menu_choice !="5":
            print("\nInvalid Input! Pick a choice listed in the menu.\n")