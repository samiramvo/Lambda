def trier(liste,n):
    return sorted(liste,key=lambda x:x[n])

liste=[('Greyson Fulton',98,99),('Brady Ken',97,96),('Beau Turnbull',94,98)]

print(trier(liste,1))