def legkisebb():
    i=2520
    while True:
        if i%19==0 and i%18==0 and i%17==0 and i%16==0 and i%15==0 and i%14==0 and i%13==0 and i%12==0 and i%11==0:
            return i
        i+=2520
print(legkisebb())

def legkisebb():
    i=2520
    flag=0
    while True:
        for j in range(11,20):
            if i%j==0:
                flag=1
            else:
                flag=0
                break
        if flag==1:
            return i

        i+=2520
print(legkisebb())
