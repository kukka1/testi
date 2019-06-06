luku = int(input("Anna luku.\n"))

if luku > 0:
    print("Luku on positiivinen.")
    if luku > 10:
        print ("Luku on suurempi kuin kymmenen.")
elif luku < 0:
    print("Luku on negatiivinen.")
    if luku < -10:
        print ("Luku on pienempi kuin miinus kymmenen.")
else:
    print("Luku 0 ei ole positiivinen eikä negatiivinen.")
print ("Ohjelman suoritus päättyy.")    