# 🏰 Jeu d'aventure Python – "Forêt des Monstres"

Un mini-jeu textuel en Python où vous incarnez un aventurier courageux explorant une forêt pleine de dangers.  
Votre mission : **vaincre 5 monstres avant que vos points de vie (PV) ne tombent à zéro !**

---

## 🎮 Fonctionnement du jeu

Au lancement, vous commencez avec **100 PV** et **0 monstre vaincu**.  
À chaque tour, un **événement aléatoire** se produit :

- 👹 **Un monstre apparaît** :  
  Vous pouvez **combattre (c)** ou **fuir (f)**.  
  - Si vous combattez, vous perdez entre 15 et 25 PV.  
  - Si vous fuyez, vous perdez entre 0 et 5 PV.  

- 🧪 **Une potion magique apparaît** :  
  Vous pouvez choisir de **la boire (o)** ou **non (n)**.  
  - Si vous la buvez, vous gagnez (ou parfois perdez) entre -10 et +15 PV.

Vous pouvez **quitter le jeu à tout moment** en entrant la commande **q**.

---

## 🧾 Conditions de victoire et de défaite

- 🏆 **Victoire :** Vous avez vaincu 5 monstres.
- 💀 **Défaite :** Vos PV tombent à 0 ou moins.
- 👋 **Abandon :** Vous entrez `q` à tout moment pour quitter le jeu.

---

## ⚙️ Installation et exécution

### 1. Prérequis
- Python 3 installé sur votre machine

### 2. Exécution
1. Téléchargez le fichier du jeu, par exemple :foret_des_monstres.py
2. Dans un terminal, exécutez :
```bash
python foret_des_monstres.py
