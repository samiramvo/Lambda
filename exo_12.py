liste=[-1,2,-3,5,7,8,9,-10]
liste1=[i for i in liste if i%2==0]
liste2=[i for i in liste if i%2==1]
func=lambda x,y:x.extend(y)
print(func(liste1,liste2))