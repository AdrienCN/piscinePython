import sys

languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
for key, value in languages.items():
    print("{} was created by {}".format(key, value))
