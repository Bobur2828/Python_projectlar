def farq(a, b):
    farqlik = ""
    
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                farqlik += b[i]
        return farqlik
    elif len(a) < len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                farqlik += b[i]
        return farqlik + b[len(a):]
    elif len(a) > len(b):
        for i in range(len(b)):
            if a[i] != b[i]:
                farqlik += b[i]
        return farqlik + a[len(b):]


print(farq("Olamshumul", "Olamshimol"))  # "io"
print(farq("Olamshumul", "Olamshum"))    # "ul"
print(farq("Olamshumul", "Olamshimullar")) # "ilar"
print(farq("aa", "a")) # "a"

