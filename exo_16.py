n=int(input("Entrez le nombre d'élève:"))
liste=[]

for i in range(n):
    name=input("Name:")
    score=int(input("Niveau:"))
    liste.append([name,score])

func=list(filter(lambda x:x[1]))
print(func)