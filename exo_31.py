liste=['Python','list','practice','solution']
print(liste)
n=int(input("Longueur de la chaine à extraire:"))

func=list(filter(lambda x:len(x)==n,liste))

print(func)