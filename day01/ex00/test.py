import sys
import time
from recipe import Recipe
from book import Book

recipe_one = Recipe("Soupe de Cresson",
                    3,
                    15,
                    ["Eau", "Cresson", "Sel"],
                    "C'est pas tres bon la soupe de cresson",
                    "lunch")

recipe_two = Recipe("Sandwich",
                    1,
                    5,
                    ["Pain", "Jambon", "Beurre"],
                    "Un bon gros jambon beurre",
                    "starter")

recipe_three = Recipe("Glace",
                      2,
                      20,
                      ["Eau", "Sucre", "Lait"],
                      "Une glace sans saveur au Lait",
                      "dessert")
book = Book("Recette de Mamie")

# Livre a son initialisation
print(str(book))

# sleep pour voir le changement de last_update
time.sleep(1)

book.add_recipe(recipe_one)
book.add_recipe(recipe_two)
book.add_recipe(recipe_three)

book.add_recipe("test")


# print all dessert
print("\n****\t@All Starter :\t****")
for i in book.get_recipes_by_types("starter"):
    print(str(i), "----", sep="\n")

# ERROR CHECK
print("\n****\tERROR CHECK (lunc instead of lunch) --> @All Lunch  :\t****")
for i in book.get_recipes_by_types("lunc"):
    print(str(i), "----", sep="\n")

# print all dessert
print("\n****\t@All Desert :\t****")
for i in book.get_recipes_by_types("dessert"):
    print(str(i), "----", sep="\n")

# print recipe by name
print("\nSearching recipe by name, enter a name:")
name = input()
book.get_recipe_by_name(name)

# Check upate time change
print("\n****Check update time *****")
print(str(book), "\n")
