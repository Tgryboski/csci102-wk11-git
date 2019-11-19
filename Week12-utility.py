


def PrintOutput(out):
    print('OUTPUT', out)


def LoadFile(nm):
    nm = open(nm, 'r')
    out = []
    for lin in nm:
        out.append(lin)
    return out


def UpdateString(orig, let, ind):
    origl = []
    for l in orig:
        origl.append(l)
    origl[ind] = let
    orig = ''
    for l in origl:
        orig += l
    return orig


def FindWordCount(lis, burd): #because thebird is theword
    out = 0
    for w in lis:
        if w == burd:
            out += 1
    return out


def ScoreFinder(lys, scor, nam):
    out = 'player not found'
    for p in range(0, len(lys)-1):
        if nam.lower() == lys[p].lower():
            out = ('%s got a score of %d' % (lys[p], scor[p]))
    return out
            
