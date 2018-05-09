def fordito():
    fordit = input("Hogyan szeretne forditani?\n(PigLatinrol vagy Piglatinra)\n")
    mondat = input("Adjon meg egy mondatot: ")
    szavak = mondat.split(" ")
    if fordit=="PigLatinra":
        PigLatin = ""
        szavak[0]=szavak[0].replace(szavak[0],szavak[0].lower())
        szavak[0]=szavak[0].replace(szavak[0][1],szavak[0][1].upper())

        for i in range(len(szavak)):
            PigLatin+=szavak[i][1:]+szavak[i][0]+"ay "
        PigLatin=PigLatin[0:-1]
        return PigLatin
    elif fordit=="PigLatinrol":
        s=""
        szavak[0] = szavak[0].replace(szavak[0], szavak[0].lower())
        szavak[0] = szavak[0].replace(szavak[0][-3], szavak[0][-3].upper())
        for i in range(len(szavak)):
            s+=szavak[i][-3]+szavak[i][:-3]+" "
        return s
print(fordito())
