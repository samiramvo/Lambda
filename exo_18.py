liste=['php','w3r','Python','abcd','Java','aaa']
func=list(filter(lambda x:x==x[::-1],liste))
print(func)