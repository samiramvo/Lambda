def tuple_str(tuple1):
    return tuple(map((lambda x:(int(x[0]),int(x[2]))),tuple1))

tuple2=(('233','ABCD','33'),('1416','EFGH','55'),('2345','WERT','34'))
print(tuple_str(tuple2))