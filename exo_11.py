liste1=[1,2,3,5,7,8,9,10]
liste2=[1,2,4,8,9]

func=(lambda liste1,liste2: set(liste1)& set(liste2))

print(list((func(liste1,liste2))))