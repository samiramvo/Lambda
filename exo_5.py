liste=[1,2,3,4,5,6,7,8,9,10]

func=list(filter(lambda x:x%2==0,liste))
func2=list(filter(lambda x:x%2==1,liste))

print("Les nombres pairs:",list(func))
print("Les nombres impairs:",list(func2))