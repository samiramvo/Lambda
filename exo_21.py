liste=[2,4,6,8,5,6]
print(liste)
n=int(input("Entrez le nombre pour effectuer la multiplication:"))
func=list(map(lambda x:x*n,liste))
print(func)