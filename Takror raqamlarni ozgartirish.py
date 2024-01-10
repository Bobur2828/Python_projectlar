
def tartib(my_list):
    b = []
    
    for i in my_list:
        if i in b:
            b.append("_")
        else:
            b.append(i)
    z = [x for x in b if type(x) == int]
    c = [c for c in b if c == "_"]
    return sorted(z) + c
print(tartib([4,1,5,1,8,5,4]))  # Natija [1, 4, 5, 8, '_', '_', '_']

