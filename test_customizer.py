import unittest
import unittest.mock
#from pet import *
from customizer import *

class TestCustomizer(unittest.TestCase):
    def test_concrete_pet_getter(self):
        p = Concrete_Pet()

        self.assertEqual(p.get_pants(), "Pants: ")
        self.assertEqual(p.get_shirt(), "Shirt: ")
        self.assertEqual(p.get_hat(), "Hat: ")
    
    def test_concrete_pet_setter(self):
        p = Concrete_Pet()

        self.assertEqual(p.set_pants(), "None")
        self.assertEqual(p.set_shirt(), "None")
        self.assertEqual(p.set_hat(), "None")

    def test_Jeans(self):
        p = Concrete_Pet()
        p = Jeans(p)

        self.assertEqual(p.get_pants(), "Pants: Jeans 👖")
        self.assertEqual(p.get_shirt(), "Shirt: ")
        self.assertEqual(p.get_hat(), "Hat: ")
    
    def test_Skirt(self):
        p = Concrete_Pet()
        p = Jeans(p)

        self.assertEqual(p.get_pants(), "Pants: Jeans 👖�")
        self.assertEqual(p.get_shirt(), "Shirt: ")
        self.assertEqual(p.get_hat(), "Hat: ")
    
    def test_Tank(self):
        p = Concrete_Pet()
        p = TankTop(p)

        self.assertEqual(p.get_pants(), "Pants: ")
        self.assertEqual(p.get_shirt(), "Shirt: Tank Top 🎽")
        self.assertEqual(p.get_hat(), "Hat: ")

    def test_Beanie(self):
        p = Concrete_Pet()
        p = Beanie(p)

        self.assertEqual(p.get_pants(), "Pants: ")
        self.assertEqual(p.get_shirt(), "Shirt: ")
        self.assertEqual(p.get_hat(), "Hat: Beanie 🧢")

    def test_Skirt_and_TShirt(self):
        p = Concrete_Pet()
        p = Jeans(p)
        p = TShirt(p)

        self.assertEqual(p.get_pants(), "Pants: Jeans 👖")
        self.assertEqual(p.get_shirt(), "Shirt: T-Shirt 👚")
        self.assertEqual(p.get_hat(), "Hat: ")

    def test_Skirt_and_TShirt_beanie(self):
        p = Concrete_Pet()
        p = Jeans(p)
        p = TShirt(p)
        p = Beanie(p)

        self.assertEqual(p.get_pants(), "Pants: Jeans 👖")
        self.assertEqual(p.get_shirt(), "Shirt: T-Shirt 👚")
        self.assertEqual(p.get_hat(), "Hat: Beanie 🧢")

    def test_change_while_clothed(self):
        p = Concrete_Pet()
        p = Jeans(p)
        p = TShirt(p)
        p = Beanie(p)

        self.assertEqual(p.get_pants(), "Pants: Jeans 👖")
        self.assertEqual(p.get_shirt(), "Shirt: T-Shirt 👚")
        self.assertEqual(p.get_hat(), "Hat: Beanie 🧢")

        p = Skirt(p)
        p = TankTop(p)
        p = Crown(p)

        self.assertEqual(p.get_pants(), "Pants: Skirt 👗")
        self.assertEqual(p.get_shirt(), "Shirt: Tank Top 🎽")
        self.assertEqual(p.get_hat(), "Hat: Crown 👑")
