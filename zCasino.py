import math
import random
import os

vTirage = 0
vPari = 0
vMontant = 0.00

def Mise():
    vMontant= input("Saisissez le montant : ")
    vPari = input("Saisissez votre pari : " )

def Tirage(vTirage=0):
    vTirage = int(random.randrange(50))
    print("Le Tirage est de " +
          str(vTirage))

def Resultat():
    print(vTirage)
    vPaire = False
    if vTirage/2 == math.ceil(vTirage/2):
        vPaire = True
    if vTirage == vPari:
        print("Gagné")
    else:
        print("Perdu")

if __name__ == '__main__':
    Mise()
    Tirage()
    Resultat()
    os.system("pause")

