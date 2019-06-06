print ("Ohjelma laskee kolmen luvun keskiarvon.")
luku1_mj = input("Anna 1.luku.")
luku1_kl = int(luku1_mj)

luku2_kl = int(input("Anna 2.luku."))
                     
luku3_kl = int(input("Anna 3.luku."))

keskiarvo = (luku1_kl + luku2_kl + luku3_kl) /3

print("Lukujen keskiarvo:", "{:.2f}" .format(keskiarvo))