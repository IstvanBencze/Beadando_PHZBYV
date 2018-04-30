def fordito(mondat):
    PigLatin=""
    szavak=mondat.split(" ")
    for i in range(len(szavak)):
        PigLatin+=szavak[i]+szavak[i][0]+"ay "
    return PigLatin
print(fordito("The quick brown fox"))
