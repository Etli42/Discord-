import random 

def sifre_uret(uzunluk):
    semboller = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    parola = ""
    for i in range(uzunluk):
        parola += random.choice(semboller)

    return parola