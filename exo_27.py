def sort_list(liste):
    return [sorted(x,lambda x:x[0]) for x in liste]

liste=[["green","orange"],["black","white"],["white","black","orange"]]
print(sort_list(liste))