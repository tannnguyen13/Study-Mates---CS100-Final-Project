from unittest import mock
from mock import patch, MagicMock
import sys
import io
import time
from unittest import TestCase
from pet import *

class TestPet(TestCase):
    def test_pet_default(self):
        p = Pet()
        defaultName = p.getName()
        dmaxLevel = p.getMaxLevel()
        dExp = p.getExp()
        dLevel = p.getLevel()

        self.assertEqual(defaultName, "Default")
        self.assertEqual(dmaxLevel, 0)
        self.assertEqual(dExp, 0)
        self.assertEqual(dExp, 0)
        self.assertEqual(dLevel, 0)
    
    def test_pet_settypeFire(self):
        f = Pet()
        f = set_type(f,"fire")
        name = f.getName()
        level = f.getLevel()
        exp = f.getExp()
        maxlevel = f.getMaxLevel()

        self.assertEqual(name, "fire")
        self.assertEqual(level, 1)
        self.assertEqual(exp, 0)
        self.assertEqual(maxlevel, 5)
    
    def test_pet_settypeWater(self):
        f = Pet()
        f = set_type(f,"water")
        name = f.getName()
        level = f.getLevel()
        exp = f.getExp()
        maxlevel = f.getMaxLevel()

        self.assertEqual(name, "water")
        self.assertEqual(level, 1)
        self.assertEqual(exp, 0)
        self.assertEqual(maxlevel, 4)

    def test_pet_settypeGrass(self):
        f = Pet()
        f = set_type(f,"grass")
        name = f.getName()
        level = f.getLevel()
        exp = f.getExp()
        maxlevel = f.getMaxLevel()

        self.assertEqual(name, "grass")
        self.assertEqual(level, 1)
        self.assertEqual(exp, 0)
        self.assertEqual(maxlevel, 3)
    
    def test_pet_levelFire(self):
        p = firetype()
        currentLevel = p.getLevel()
        currentExp = p.getExp()
        self.assertEqual(currentExp, 0)
        self.assertEqual(currentLevel, 1)

        p.gainExp(25)
        currentLevel = p.getLevel()
        currentExp = p.getExp()
        self.assertEqual(currentExp, 50)
        self.assertEqual(currentLevel, 1)

        p.gainExp(75)
        currentLevel = p.getLevel()
        isMax = p.check_max_level()
        self.assertEqual(currentExp, 50)
        self.assertEqual(currentLevel, 4)
        self.assertEqual(isMax, False)