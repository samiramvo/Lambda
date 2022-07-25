liste=[('Greyson Fulton',98,99),('Brady Ken',97,96),('Beau Turnbull',94,98)]
print(liste)
n=int(input("Extraire l'element: "))
func=list(map(lambda x:x[n],liste))
print(func)
