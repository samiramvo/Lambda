liste=[[1,2,3],[2,4,5],[1,1,1]]

def tri_som(liste):
    return sorted(liste,key=lambda x:x[0]+x[1]+x[2])

print(tri_som(liste))