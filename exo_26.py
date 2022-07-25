liste=[[0],[1,3],[5,7],[9,11],[13,15,17]]
func=lambda x:tuple(max(len(x) for x in liste))
func1=lambda x:tuple(min(len(x) for x in liste))
print(func(liste))
print(func1(liste))