def divisible(num,num2):
    return [n for n in range(num,num2+1)
          if not(any(map(lambda x:int(x)==0 or n%int(x)!=0,str(n))))]

print(divisible(1,22))


