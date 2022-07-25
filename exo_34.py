dico={
    'Cierra Vega':(6.2,70),
    'Alden Cantrell':(5.9,65),
    'Kierra Gentry':(6.0,68),
    'Cox':(5.8,66)
}

func=dict(filter(lambda x:(x[1][0],x[1][1])>(6.0,70),dico.items()))
print(func)

