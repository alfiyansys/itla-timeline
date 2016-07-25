#!/usr/bin/python

m = 30
k = 3
h = 60

ba = m + k + h + k
print "lama fase " + str(ba) + " detik "

def stateTL(dt):
    cpmk = m
    cpkh = m + k
    cphk = m + k + h
    cpkm = m + k + h + k

    if dt >= 0 and dt < cpmk:
        return "merah"
    elif dt >= cpmk and dt < cpkh:
        return "kuning"
    elif dt >= cpkh and dt < cphk:
        return "hijau"
    elif dt >= cphk and dt < cpkm:
        return "kuning"
    else:
        return "udv"


for num in range(0,ba):
    print str(num) + " = " + stateTL(num)
