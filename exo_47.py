def sort_mixed_list(liste):
    return sorted(liste,key=lambda e:(isinstance(e,str),e))

liste=[18,96,7,8,"Sami",None,"white","green"]
print(sort_mixed_list(liste))