import sys


def check_recipe_type(recipe_type):
    if (recipe_type == "dessert"
        or recipe_type == "lunch"
            or recipe_type == "starter"):
        return True
    else:
        return False


class Recipe:
    """Class containing infos about a recipe"""
    def __init__(self, recipe_name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        # check recipe_name input
        assert isinstance(recipe_name, str), "recipe_name must be string"
        assert len(recipe_name) > 0, "recipe_name cannot be empty"

        # check cooking_lvl input
        assert isinstance(cooking_lvl, int), "cook_lvl must be an int"
        assert (cooking_lvl >= 1 and cooking_lvl <= 5), "cook_lvl must "\
                                                        "be between 1 and 5"

        # check cooking_time input
        assert isinstance(cooking_time, int), "cook_time must be an int"
        assert cooking_time >= 0, "cook_time must be >= 0"

        # check ingredient input
        assert isinstance(ingredients, list), "ingredients must be a list"
        assert len(ingredients) > 0, "ingredients cannot be empty"
        for i in ingredients:
            assert isinstance(i, str), "Every list item must be a string"

        # check description input
        assert isinstance(description, str), "description must be a string"

        # check recipe type input
        assert isinstance(recipe_type, str), "Recipe_type must be a string"
        assert check_recipe_type(recipe_type), "Recipe_type must be "\
                                               "dessert, lunch or starter"

        # assign value if all true
        self.name = recipe_name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ("Recipe name : " + self.name +
               "\ncooking_lvl : " + str(self.cooking_lvl) +
               "\ncooking_time : " + str(self.cooking_time) + "min(s)"
               "\ningredients: " + ", ".join(self.ingredients) +
               "\ndescription : " + self.description +
               "\ntype of meal : " + self.recipe_type)
        return txt
