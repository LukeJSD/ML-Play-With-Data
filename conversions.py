def Time(t):
    if type(t)==str:
        t = t.split(':')
        out = 0
        out += float(t[0])*60
        out += float(t[1])
        return out
    else:
        return str(int(t//60))+':'+str(t%60)
