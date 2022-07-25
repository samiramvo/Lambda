from collections import Counter
liste=["red","black","white","green","orange"]
print(liste)
x=input("Chaine à trouver:")

func=list(filter(lambda a,x:x in a,liste))

print(func)