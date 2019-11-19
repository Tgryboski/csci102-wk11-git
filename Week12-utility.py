


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


