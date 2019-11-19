


def PrintOutput(out):
    print('OUTPUT', out)


def LoadFile(nm):
    nm = open(nm, 'r')
    out = []
    for lin in nm:
        out.append(lin)
    return out


