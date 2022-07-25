def intersection(liste1,liste2):
    return [list(filter(lambda x:x in liste1 ,sublist)) for sublist in liste2]

print(intersection([1,2,3,4,5,6,7,8,9,10,11,12,13,14],[[12,18,23,25,45],[7,11,19,24,28]]))
