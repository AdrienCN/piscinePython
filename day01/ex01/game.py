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
        self.is_alive = False if self.is_alive else True


faceless = GotCharacter()
print(faceless.__dict__)

oberyn = Martell("Oberyn")
print(oberyn.__doc__)
print(oberyn.__dict__)
oberyn.print_house_words()
print(oberyn.is_alive)
oberyn.die()
print(oberyn.is_alive)
