print("Tri d'une liste:")
print("Voici une liste:")
liste=[("English",88),("Science",90),("Math",97),("Social sciences",82)]
print(liste)
tri=liste.sort(lambda x:x[1])
print("La liste trié donne:")
print(list(tri))