liste=['orange','rouge','vert','bleu','noir',None,6,9,5,None,None]

def rem_list(liste):
    return list(filter(lambda x:x is not None,liste))

print(rem_list(liste))