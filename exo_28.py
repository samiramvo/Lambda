liste=[[2],[0],[1,3],[0,7],[9,11],[13,15,17]]

def trier(liste):
    return sorted(liste,lambda x: (len(x),x) )
liste1=trier(liste)

print(liste1)