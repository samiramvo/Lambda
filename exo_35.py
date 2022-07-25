liste=[1,2,4,6,8,10,12,14,16,17]
liste1=[5,8,4,0]

func=list(map(lambda x:x==x.sort(),liste))

print(func)
