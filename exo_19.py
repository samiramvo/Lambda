
from collections import Counter
liste=['bcda','abce','cbea','adcb']

func=list(filter(lambda x: Counter("abcd")==Counter(x),liste))
print(func)