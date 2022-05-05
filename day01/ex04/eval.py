import sys


def check_input(coefs, words):
    if not isinstance(words, list) or not isinstance(coefs, list):
        print("Error: coefs and words must be list")
        return 0
    if not all(isinstance(x, (int, float)) for x in coefs):
        print("Error : coefs must be float or int list")
        return 0
    if not all(isinstance(x, str) for x in words):
        print("Error : words must be string list")
        return 0
    if not len(words) == len(coefs):
        return 0
    return 1


class Evaluator:

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not check_input(coefs, words):
            return -1
        res = 0
        # tup[0] = index | tup[1] = valeur de l'iterateur
        for tup in enumerate(words):
            res += len(tup[1]) * coefs[tup[0]]
        return res

    @staticmethod
    def zip_evaluate(coefs, words):
        if not check_input(coefs, words):
            return -1
        t = zip(coefs, words)
        res = 0
        for i in t:
            res += i[0] * len(i[1])
        return res


words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 5.0]

print("Word = ", words)
print("Coef = ", coefs, "\n")
print("ZIP : ", Evaluator.zip_evaluate(coefs, words))
print("\t********")
print("ENUMERATE : ", Evaluator.enumerate_evaluate(coefs, words))
