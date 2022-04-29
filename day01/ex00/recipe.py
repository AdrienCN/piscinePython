import sys


class Recipe:
    """This is a class describing a recipe""" 
    # string 
        # name
    # range 1 to 5 
        # cooking_lvl
    # non negative int 
        # cooking_time
    # list[]
        # ingredient = []
    # str
        # description = ""
    # str starter - lunch - dessert 
        #recipe_type = ""

    def __init__(self, recipe_name, cooking_lvl, cooking_time, 
                 ingredient, description, recipe_type):
        assert isinstance(recipe_name, str), "First arg (recipe_name)  must be string"
        assert len(recipe_name) > 0, "First arg(recipe_name) cannot be empty"

        assert isinstance(cooking_lvl, int), "Second arg (cook_lvl) must be an int"
        assert (cooking_lvl > 0 and cooking_lvl < 6), "Second arg (cook_lvl) must be between 1 and 5"
        
        assert isinstance(cooking_time, int), "Third arg (cook_time) must be an int"
        assert cooking_time >= 0, "Third arg (cook_time) must be >= 0"

        assert isinstance(ingredient, list), "Fourth arg (ingredient)  must be a list"
        assert len(ingredient) > 0, "Fourth arg (ingredient) cannot be empty"
        for i in ingredient:
            assert isinstance(i, str), "Every list item must be a string"

        assert isinstance(description, str), "Fifth arg (description) must be a string"
        assert isinstance(recipe_type, str), "Sixth arg (recipe_type) must be a string"
        assert (recipe_type  == "dessert" 
            or recipe_type == "lunch" 
            or recipe_type == "starter"), "Sixth argi (recipe_type)  must be dessert, lunch or starter"
        
        self.name = recipe_name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredient = ingredient
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return exhaustive recipe information"""
        ret = ("Recipe:\nname : " + self.name +  
              "\ncooking_lvl : " + str(self.cooking_lvl) +  
              "\ncooking_time : " + str(self.cooking_time) + "min(s)"
              "\ningredients: " + ", ".join(self.ingredient) + 
              "\ndescription : " + self.description +
              "\ntype of meal : " + self.recipe_type)
        return ret
