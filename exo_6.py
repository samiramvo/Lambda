liste=[1,2,3,4,5,6,7,8,9,10]
print(liste)
carre=list(map(lambda x :x**2,liste))
cube=list(map(lambda x:x**3 , liste))
print("Le carre de la liste:",carre)
print("Le cube de la liste:",cube)