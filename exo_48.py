liste=['4','12','5','0','7','-10']

def tri_num(liste):
    return sorted(liste,key=(lambda x:int(x)))

print(tri_num(liste))