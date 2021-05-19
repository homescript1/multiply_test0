def multiply1_msg():
    return "Le résultat du calcul est"

def multiply_msg():
    return "Table de multiplication de"

def division_msg():
    return "Le résultat de cette division est"

def multiply(n, x):
    #entiers = [n, x]
    #nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #for entier in entiers :
    if -1 < n < 13 and -1 < x < 13:
        return n * x
    #elif x < 13:
        #return n * x
    else:
        print("Valeur(s) trop élevée(s)!\nJe ne prend en compte que des nombres positifs inférieurs à 13!")

def MULTIPLICATION_1():
    print("1-CALCUL DE MULTIPLICATION")
    n = int(input("Entrer un premier nombre: "))
    x = int(input("Entrer un second nombre: "))
    multiply_result = multiply(n, x)
    print(multiply1_msg(), multiply_result)

def MULTIPLICATION_2():
    print("2-TABLE DE MULTIPLICATION")
    chiffre = int(input("Entrez un chiffre/nombre quelconque: "))
    print(multiply_msg(), chiffre)
    for num in range(0, 13):
        print(chiffre, "x", num, "= {}".format(chiffre * num))


num1 = 1
num2 = 2
while num1 and num2 in range(1, 3):
    choix = int(input("Multiplication 1 ou 2 ? "))
    if choix == num1:
        MULTIPLICATION_1()
        print("Fin du programme!")
        break
    elif choix == num2:
        MULTIPLICATION_2()
        print("Fin du programme!")
        break
    else:
        print("Veuillez choisir entre 1 et 2...")
