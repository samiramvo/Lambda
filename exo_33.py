from itertools import re
func=lambda x: True if re.search("[A-Z],[0-9],[a-z],x") else False

print(func)