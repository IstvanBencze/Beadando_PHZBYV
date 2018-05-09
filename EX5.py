def szazas():
    s=""
    for i in ("+","-",""):
        for i2 in ("+", "-", ""):
            for i3 in ("+", "-", ""):
                for i4 in ("+", "-", ""):
                    for i5 in ("+", "-", ""):
                        for i6 in ("+", "-", ""):
                            for i7 in ("+", "-", ""):
                                for i8 in ("+", "-", ""):
                                    s="1"+i+"2"+i2+"3"+i3+"4"+i4+"5"+i5+"6"+i6+"7"+i7+"8"+i8+"9"
                                    if eval(s)==100:
                                        print(s,end="=100\n")
szazas()
