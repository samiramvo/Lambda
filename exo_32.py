liste=[1,'abcd',3.12,1.2,4,'xyz',5,'pqr',7,-5,-12.22]

func=list(filter(lambda x:isinstance(x,float),liste))
print(len(func))