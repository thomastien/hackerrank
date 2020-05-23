def vercomp(x,y):
    xnums = x.split('.')
    ynums = y.split('.')

    majorx = xnums[0]
    majory = ynums[0]

    minorx = xnums[1] if len(xnums) > 1 else None
    minory = ynums[1] if len(ynums) > 1 else None

    revisionx = xnums[2] if len(xnums) > 2 else None
    revisiony = ynums[2] if len(ynums) > 2 else None


    for i in range(3):
        x = xnums[i] if len(xnums) > i else None
        y = ynums[i] if len(ynums) > i else None 
        #print('comparing ', x, ' vs ', y)
        if x is None:
            return -1
        if y is None:
            return 1
        if int(x) > int(y):
            return 1
        elif int(x) < int(y):
            return -1
        else:
            # must be equal, continue
            pass

    return 1


    #if int(majorx) > int(majory):
    #    return 1
    #elif int(majorx) == int(majory):
    #    if int(minorx) > int(minory):
    #        return 1
    #    elif int(minorx) == int(minory):
    #        if int(revisionx) > int(revisiony):
    #            return 1
    #        else:
    #            return -1
    #    else:
    #        return -1
    #else:
    #    return -1 


def solution(l):
    return sorted(l,cmp=vercomp)

