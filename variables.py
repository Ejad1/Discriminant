def va():
    a = input("Entrez la valeur de a (a est différent de zéro):")
    if not a.isdigit() or a == '0' :
        print("Vous n'avez pas entrez un chiffre valide.")
        return va()
    else:
        return a

def vb():
    b = input("Entrez la valeur de b :")
    if not b.isdigit():
        print("Vous n'avez pas entrez un chiffre pour b")
        return vb()
    else:
        return b

def vc():
    c = input("Entrez la valeur de c :")
    if not c.isdigit():
        print("Vous n'avez pas saisi un chiffre")
        return vc()
    else:
        return c
        