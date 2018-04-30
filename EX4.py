def fordito(mondat):
    PigLatin=""
    szavak=mondat.split(" ")
    szavak[0]=szavak[0].replace(szavak[0],szavak[0].lower())
    szavak[0]=szavak[0].replace(szavak[0][1],szavak[0][1].upper())
    for i in range(len(szavak)):
        PigLatin+=szavak[i]+szavak[i][0]+"ay "
    return PigLatin
print(fordito("The quick brown fox"))
