# -*-coding:Latin-1 -*
import math
import os

def Bisextile():
    annee = input("Saisissez une année : ")  # On attend que l'utilisateur fournisse l'année qu'il désire tester
    annee = int(annee)  # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print("L'année saisie est bissextile.")
    else:
        print("L'année saisie n'est pas bissextile.")
def test(nb: object = 9) -> object:  # Test Racine carrée

    print(math.sqrt(nb))




if __name__ == '__main__':
    try:
        test(25)
        Bisextile()
        os.system("pause")
    except type_de_l_exception as exception_retournee:
        print("Voici l'erreur :", exception_retournee)