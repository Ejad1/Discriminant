from cmath import sqrt
from variables import *
import os
print("Nous cherchons les solutions éventuelles d'une équation de la forme ax^2 + bx + c = 0 \n")

a = va()
b = vb()
c = vc()
 
a = int(a)
b = int(b)
c = int(c)

# On s'attaque maintenant aux conditions
if a == 1:
    if b == 0 and c == 0:
        print("L'équation est x^2")
    elif b == 0 and c == 1:
        print("L'équation est x^2 + 1")
    elif b == 0 and c != 0 and c != 1:
        print("L'équation est x^2 +", c)
    elif b == 1 and c == 0:
        print("L'équation est x^2 + x")
    elif b == 1:
        print("L'équation est x^2 + x +", c,)

        # Maintenant on passe au cas où a est différent de 0 et 1
elif a != 0 and a != 1:
    if b == 0:
        if c == 0:
            print("L'équation est", a, "x^2")
        elif c == 1:
            print("L'équation est", a, "x^2 + 1")
        else:
            print("L'équation est", a, "x^2 +", c)
    elif b == 1:
        if c == 0:
            print("L'équation est", a, "x^2 + x")
        elif c == 1:
            print("L'équation est", a, "x^2 + x + 1")
        else:
            print("L'équation est", a, "x^2 + x +", c)
    else:
        if c == 0:
            print("L'équation est", a, "x^2 +", b, "x")
        elif c == 1:
            print("L'équation est", a, "x^2 +", b, "x + 1")
        else:
            print("L'équation est", a, "x^2 +", b, "x +", c)

a = int(a)

delta = b**2 - 4*a*c

if delta < 0:
    print("Le discriminant vaut", delta, "et est inférieur à zéro. Cette équation n'admet pas de solutions réelles. \n")
elif delta == 0:
    print("Le discriminant est égal à zéro. Cette équation admet donc une solution double. \n")
    sol0 = -b/(2*a)
    print("Cette solution est :", sol0, "\n")
else:
    print("Le discriminant vaut", delta, "et est supérieur à zéro. \n")
    if a != 0:
        x1 = (-b-sqrt(delta))/(2*a)
        x2 = (-b+sqrt(delta))/(2*a)
        print("Cette équation admet donc deux solutions réelles x1 et x2. \n")
        print("x1 =", x1, "et x2 =", x2)
    else:
        print("Oups...a est égale à zéro. Il est donc impossible de calculer les deux solutions!!! \n")

os.system("pause")
