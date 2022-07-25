liste=[('V',62),('VI',68),('VII',70),('IX',74),('X',65)]

def max_min(liste):
    max_liste=max(enumerate(liste),key=(lambda x:x[1]))
    min_liste=min(enumerate(liste),key=(lambda x:x[1]))
    return max_liste,min_liste

print(max_min(liste))
