#import pet
#import timer
#from pet import *
#from timer import timer
from timer import *
from menu import *
from pet import *
#from customizer import *

if __name__ == "__main__":
    user = open("user1.txt","r")
    if user.readline() is not ""
        user1 = open("user1.txt","a")
        total = 0
        menu_choice = "1"
        me = Pet()
        name = input(" Enter your username: ")
        passw = input(" Enter your password: ")
        user1.write(str(name)+'\n')
        user1.write(str(passw)+'\n')

    Welcome()
    

    while menu_choice != "5":
        menu()
        menu_choice = input("Pick a menu choice \n")

        if menu_choice == "1":
            type = input("Pick your pet type! (Fire🔥), (Water🌊), (Grass🍃) \n")
            me = set_type(me, type)

            name = input("What do you want to name your pet? \n")
            me.changeName(name)
            me.petIntro()

            user1.write(name.lower()+'\n')
            user1.write(type.lower()+'\n')
            
            time = Timer()
            time.run_timer()
            
            total += time.return_total_time()
            me.gainExp(time.return_total_time())

            me.petIntro()
            if me.check_max_level() == True:
                print("Congratulations! I have reached my max level! 😇🙏🏼")

            user1.write(str(me.level)+'\n')
            user1.write(str(me.exp)+'\n')

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
        if menu_choice == "4":
            """custom = FireCustomizer(me)
            custom.customizer(me)"""
        if menu_choice == "5":
            print("Goodbye!")
        elif menu_choice not in ("1" or "2" or "3" or "4" or "5"):
            print("\nInvalid Input! Pick a choice listed in the menu.\n")
