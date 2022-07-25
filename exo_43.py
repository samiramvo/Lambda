from functools import reduce
def mult(liste):
    return reduce (lambda x,y:x*y,liste)

liste=[1,6,4,3,2]

print(mult(liste))