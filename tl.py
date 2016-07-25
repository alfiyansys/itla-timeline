#!/usr/bin/python
# Code by M. Alfiyan Syamsuddin
# Problem description:
# Pemrosesan hanya terjadi pada hijau
# waktu default tidak berubah, hanya dikurangi sesuai dengan nilai pengurangan @tambahan {code ifal}
#

import time, threading

dh = 5 # default waktu hijau
m = 5
k = 1
h = dh

ba = m + k + h + k
print "lama fase " + str(ba) + " detik "

def process():
    print "Melakukan proses #process"
    time.sleep(3) #pemrosesan video ifal ada di sini, tidak mengganggu timeline
    # h = dh - penambahan
    print "Proses selesai #process"
    return 0

def stateTL(dt):
    cpmk = m
    cpkh = m + k
    cphk = m + k + h
    cpkm = m + k + h + k

    print "m = " + str(m) + ", k = " + str(k) + ", h = " + str(h)

    if dt >= 0 and dt < cpmk:
        #atur lampu jadi merah, di atas baris ini
        return "merah"
    elif dt >= cpmk and dt < cpkh:
        #atur lampu jadi merah + kuning, sembarang, di atas baris ini
        return "kuning"
    elif dt >= cpkh and dt < cphk:
        #atur lampu jadi hijau, di atas baris ini
        if procthread.isAlive():
            print "masih melakukan proses di detik "+str(dt)
        else:
            procthread.start()
        return "hijau | Lakukan proses di sini"
    elif dt >= cphk and dt < cpkm:
        return "kuning"
    else:
        return "udv"

procthread = threading.Thread(target=process)
print "======================= START ======================="
while 1:
    for num in range(0,ba):
        print "detik: " + str(num)
        if procthread.isAlive():
            print "thread aktif #main"
        else:
            procthread = threading.Thread(target=process)
        print "state = " + stateTL(num)
        print ""
        time.sleep(1)
    print "============= Restart Fase ==============="
