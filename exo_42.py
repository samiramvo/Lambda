from itertools import reduce
def mult(nums):
    return reduce(lambda x,y:x*y,nums,1)

print(mult([1,2,3,4,5]))