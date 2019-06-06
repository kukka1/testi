def tulosta(nimi, kertaa):
    for i in range(kertaa):
        print("Terve", nimi)

def main():
    nimi = input ("Kerro nimesi.\n")
    lkm = int(input("Kuinka mnta kertaa haluat tervehdittävän?\n"))
    
    tulosta(nimi, lkm)

main()