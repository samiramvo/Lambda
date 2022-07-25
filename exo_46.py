liste=[12,33,23,10,11,67,89,45,66.7,23,12,11,10,10.25,54]

def min_max(liste):
    func=max(enumerate(liste), key=(lambda x:x[1]))
    func1=min(enumerate(liste) ,key=lambda x:x[1])
    return func,func1


print(min_max(liste))