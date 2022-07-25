liste=['orange','rouge','vert','bleu','noir']

def rem_list(liste,remove_list):
    return list(filter(lambda x:x not in remove_list,liste))

print(rem_list(liste,['rouge','vert']))