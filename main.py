import numpy as np
from noeud import Noeud


racine = Noeud("exp")
plus = Noeud("+")
deux = Noeud(2)
y = Noeud("y")

# Assemblage de l'arbre
plus.ajouter_enfant(deux)
plus.ajouter_enfant(y)
racine.ajouter_enfant(plus)

# Verification de l'affichage polonais
# Doit afficher : "exp + 2 y"

print("Resultat :", racine.afficher_polonaise())
print()


print("--- Question 5 : evaluation ---")


variables = {"y": 0}
res = racine.evaluer(variables)
print(f"evaluation pour y = 0 : {res}")


variables = {"y": 1}
res = racine.evaluer(variables)
print(f"evaluation pour y = 1 : {res}")

# Cas 3 : Test d'erreur si une variable manque
try:
    racine.evaluer({"x": 5})  # On passe 'x' au lieu de 'y'
except ValueError as e:
    print("Erreur interceptee avec succes :", e)

print()


print("--- Question 6 : Trace de la fonction ---")

# Generation d'une liste de 100 valeurs de y entre -5 et 2
valeurs_y = np.linspace(-5, 2, 100).tolist()

# Trace de la courbe de exp(2 + y) par rapport a la variable 'y'
# (Cette commande va ouvrir une fenetre graphique matplotlib)
racine.tracer("y", valeurs_y)