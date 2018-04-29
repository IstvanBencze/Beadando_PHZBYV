def fordito(mondat):
    PigLatin=""
    for i in range(len(mondat)):
        if mondat[i]==" ":
            PigLatin+="ay "
        else:
            PigLatin+=mondat[i]
    PigLatin+="ay"
    return PigLatin
print(fordito("The quick brown fox"))
