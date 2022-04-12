import sys

languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }
for key in languages:
    print("{} was created by {}".format(key, languages[key]))
