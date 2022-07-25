

list1=[1,2,3,4,5,6,7,8,9,10]
list2=[2,4,6,8]
dif1=set(list1).difference(list2)
dif2=set(list2).difference(list1)

func=lambda x,y:x.union(y)

print(list(func(dif1,dif2)))