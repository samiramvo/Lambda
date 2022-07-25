liste=["Python",3,2,4,5,"version"]

print(max(liste,lambda x:(isinstance(int,x),x)))