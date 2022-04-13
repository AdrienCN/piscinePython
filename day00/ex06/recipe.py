import sys
#Option addrecipe a faire
cookbook = {}

def printRecipe(recipe_name):
    if recipe_name in cookbook:
        print("Recipe for {}: ".format(recipe_name))
        print("Ingredients list: {} ".format(cookbook[recipe_name]["ingredients"]))
        print("To be eaten for {}.".format(cookbook[recipe_name]["meal"]))
        print("Takes {} minutes of cooking.".format(cookbook[recipe_name]["prep_time"]))
        print("\t----------\t")
    else :
        print("Error print: This recipe does not exist")

def addRecipe(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {"ingredients" : ingredients, "meal" : meal,
                            "prep_time" : prep_time}
def delRecipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print("%s has successfully been deleted from the cookbook" %recipe_name)
    else :
        print("Error delete: <%s> does not exist in cookbook" %recipe_name)

def printCookbook():
    for recipe in cookbook:
        printRecipe(recipe)

def printMenu():
    print("""Please select an option:
            1: Add a recipe
            2: Delete a recipe
            3: Print a recipe
            4: Print the cookbook
            5: Quit""")

addRecipe("sandwich", ("bread", "ham", "cheese", "tomatoes"), "lunch", 10) 
addRecipe("cake", ("flour", "suger", "eggs"), "dessert", 60) 
addRecipe("salad", ("avocado", "arugula", "spinach", "tomatoes"), "lunch", 15)

option = 0;
while (option != 5):
    printMenu()
    option = input()
    if option == "1" :
        print("Adding recipe work in progress ...")
    elif option == "2":
        print("What recipe do you want to delete?")
        todelete = input()
        delRecipe(todelete)
    elif option == "3":
        print("What recipe do you want to print?")
        toprint = input()
        printRecipe(toprint)
    elif option == "4":
        printCookbook()
    elif option == "5":
        print("Goodbye & Thank you")
        exit()
    else:
        print("Sorry I did not understand your choice. Please restart ....")


