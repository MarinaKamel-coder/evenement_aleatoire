import random

pv=100
monstres_vaincus =0

print("Bienvenue, aventurier et aventurière ! 🏰 Tu commences avec 100 PV. Il te faut vaincre 5 monstres.")
print("\n Le choix (q) te permet de quitter le jeu à tout moment.")

while pv > 0 and monstres_vaincus < 5:
    print("""\n --- noveau tour ! ---""")
    print("\nPV restants :", pv)
    print("Monstres vaincus :", monstres_vaincus)
    print("\n Tu avances dans la forêt sombre... 🌲")

    # Événement aléatoire
    #  Deux fois plus de monstres que de potions
    evenement = random.choice(["monstre", "monstre", "potion magique"])
    if evenement == "monstre":
        degats_monstre = random.randint(15, 25)
        degats_fuite = random.randint(0, 5)
        print("😈 Un monstre surgit ! Il a une force équivalente à ", degats_monstre ," PV")
        action=input("Veux-tu le combattre (c) ou fuir (f) ? ")
        if action == "q":
            print("Tu as choisi de quitter le jeu. À bientôt ! 👋")
            break
        elif action == "c":
            print("Tu combats vaillamment le monstre ! Tu ressors victorieux, mais perds ", degats_monstre," PV.")
            pv -= degats_monstre
            monstres_vaincus += 1
        
        elif action == "f":
            print("Tu fuis et perds",degats_fuite, " PV en courant.")
            pv -= degats_fuite
        else :
            print("Action non reconnue. Tu restes sur place.")
            pv -= 0
            continue

    elif evenement == "potion magique":
        gain_potion = random.randint(-10, 15)
        action = input("🍷 Tu trouves une potion magique veux-tu la boire (o) ou non (n) ? ")
        if action == "q":
            print("Tu as choisi de quitter le jeu. À bientôt ! 👋")
            break
        elif action == "o":
             print("Tu bois la potion et gagnes ",gain_potion," PV.")
             pv += gain_potion
        
        elif action == "n":
            print("Tu as choisi de ne pas boire la potion.")
            gain_potion = 0
            pv += gain_potion       
        else:
            print("Action non reconnue. Tu restes sur place.")
            pv -= 0
            continue      

if pv<=0:
    print("\n Tu es tombé au combat... 😢")
elif monstres_vaincus >= 5:    
    print("\n Tu as vaincu 5 monstres ! Tu es un héros ! 🏆")
else:
    print("\n Tu as quitté le jeu. À bientôt ! 👋")