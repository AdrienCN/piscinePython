import sys
import time
from recipe import Recipe

class Book:
    """This is a Book full of recipe"""

    def __init__(self, name):
        assert isinstance(name, str), "Book name must be a string"
        self.name = name
        self.creation_date = time.ctime(time.time())
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def tmp(self):
        print(self.recipes_list)

    def get_recipe_by_name(self, name):
        ret_list = []
        for key in self.recipes_list:
            for i in self.recipes_list[key]:
                if i.name == name:
                    ret_list.append(i)
        return (ret_list)

    def get_recipes_by_types(self, recipe_type):
        ret = self.recipes_list.get(recipe_type)
        if len(ret) == 0:
            print("There is no %s recipe in this book" % recipe_type)
        return ret


    def add_recipe(self, recipe):
        assert isinstance(recipe, Recipe), "arg is not of Recipe type"
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = time.ctime(time.time())

    
    def __str__(self):
        ret = ("Book name : " +  self.name +
              "\nCreation date : " +  self.creation_date + 
              "\nLast update : " +  self.last_update )
        return ret

c = Recipe("Cookie", 1, 15, ["lobster", "cheese", "durian"], "Awful idea", "dessert")
a = Recipe("Cookie", 1, 15, ["lobster", "cheese", "durian"], "Bis repetita", "dessert")
b = Book("Recette Grand-Mere")
print(str(b))
time.sleep(3)
b.add_recipe(c)
b.add_recipe(a)
dessert_list = b.get_recipe_by_name("Cookie")
print(str(b))
