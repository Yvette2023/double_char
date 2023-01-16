def double_char(string):
    liste=[]
    for i in string:
        liste.append(i)
        liste.append(i)
    return "".join(liste)
print(double_char("P12ote"))