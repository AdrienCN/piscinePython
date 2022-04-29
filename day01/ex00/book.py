import sys
import time
from recipe import Recipe
from recipe import check_recipe_type


class Book:
    """Class containing multiple Recipe Class"""

    def __init__(self, name):
        assert isinstance(name, str), "Book name must be a string"
        self.name = name
        self.creation_date = time.ctime(time.time())
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the specified name and returns the instance"""
        if not isinstance(name, str):
            print("Error: to search by name, [name] must be string")
            return []
        ret_list = []
        for key in self.recipes_list:
            for i in self.recipes_list[key]:
                if i.name == name:
                    print("\n****** We found a [%s] recipe: **** \n" % name,
                          str(i), sep="")
                    ret_list.append(i)
        if len(ret_list) == 0:
            print("Sorry there is no [%s] recipe" % name)
        return (ret_list)

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        if not check_recipe_type(recipe_type):
            print("to search recipe by type, please use :",
                  "lunch, desert or starter")
            return []
        ret = self.recipes_list.get(recipe_type)
        if len(ret) == 0:
            print("There is no %s recipe in this book" % recipe_type)
        return ret

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print("Error : add recipe :  this is not a Recipe Class")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = time.ctime(time.time())

    def __str__(self):
        ret = ("Book name : " + self.name +
               "\nCreation date : " + self.creation_date +
               "\nLast update : " + self.last_update)
        return ret
