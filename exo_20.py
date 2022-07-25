liste="Sdf 23 safs8 5 sdfsd8 sdfs 56 sdfs 20 5"
print('La liste est:',liste)
print("La longueur de la liste est:")
chaine=[i for i in liste.split(" ")]
longueur=len(chaine)
print(longueur)
numbers=sorted([x for x in chaine if x.isdigit()])

func=list(filter(lambda x: x>longueur,numbers))
print(func)