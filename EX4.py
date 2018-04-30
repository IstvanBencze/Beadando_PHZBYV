def fordito(mondat):
    PigLatin=""
    tmp=""
    for i in range(len(mondat)):
        if i==0:
            tmp=mondat[0]
        else:
            if mondat[i]==" ":
                PigLatin+=tmp+"ay "
                tmp=mondat[i+1]
            else:
                PigLatin+=mondat[i]
    PigLatin+="ay"
    return PigLatin
print(fordito("The quick brown fox"))
