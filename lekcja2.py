import random

znaki = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = int(input("Podaj długośc hasła: "))
haslo = ""

#for i in range(x):
 #   haslo += random.choice(znaki)

for i in range(x):
    haslo += znaki[random.randint(0,71)]

print("Twoje wygenerowane hasło: ", haslo)