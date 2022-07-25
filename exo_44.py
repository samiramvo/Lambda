

tuple1=((10,10,10),(30,45,56),(81,80,39),(1,2,3))

def moyenne(tuple1):
    return tuple(map(lambda x:sum(x)/len(float(x),zip(*tuple1))))

print(moyenne(tuple1))
