import sys


class GotCharacter:
    """This class represents a GOT character"""

    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive


class Martell(GotCharacter):
    """This class represents a member of the Martell familly"""

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Martell"
        self.house_words = "Unbowed, Unbent, Unbroken"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


print("****Test 1 : Empty mother class****")
faceless = GotCharacter()
print(faceless.__doc__, "")
print(faceless.__dict__, "\n")

print("****Test 2 : GOTchar inheritance****")
oberyn = Martell("Oberyn")
print(oberyn.__doc__)
print(oberyn.__dict__, "\n")

print("****Test 3 :  methods ****")
oberyn.print_house_words()
print("Oberyn.is_alive = ", oberyn.is_alive)
print("Oberyn.die()")
oberyn.die()
print("Oberyn.is_alive = ", oberyn.is_alive)
