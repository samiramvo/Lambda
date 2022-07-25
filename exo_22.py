from curses.ascii import islower


liste=["Sally","Nata","sop","Fati","ete"]
func=list(filter(lambda el:el[0].isupper() and el[1:].islower(),liste))

print(len("".join(func)))
