snt = "Saya    tidak  suka,   memancing           ikan "

sntlist = snt.split()

for i in range(len(sntlist)):
    if i == 0:
        csnt = sntlist[i]
    else:
        csnt = csnt + " " + sntlist[i]

print(csnt)