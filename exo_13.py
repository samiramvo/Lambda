from itertools import count


liste=[1,2,3,4,5,6,7,8,9,10]
pairs=lambda x:x%2==0
impairs=lambda x:x%2==1
num_pairs=list(filter(pairs,liste))
num_impairs=list(filter(impairs,liste))

num=len(num_pairs)
num1=len(num_impairs)

print(num)
print(num1)