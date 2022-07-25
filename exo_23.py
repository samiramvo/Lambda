liste=[2,4,-6,-9,11,-12,14,-5,17]
print(liste)
pos=list(filter(lambda x:x>0,liste))
neg=list(filter(lambda x:x<0,liste))
print("Somme des nombres positifs:",(sum(pos)))
print("Somme des nombres positifs:",(sum(neg)))
