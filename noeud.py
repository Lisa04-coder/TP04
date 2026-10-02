import math
import matplotlib.pyplot as plt

class Noeud:
    def __init__(self, valeur):
        """
        Initialise un noeud d'un arbre d'expression.
        :param valeur: str, int ou float (nom de variable, valeur ou opérateur)
        """
        self.valeur = valeur
        self.enfants = []

    def ajouter_enfant(self, noeud_enfant):
        """Ajoute un noeud enfant à la liste des enfants."""
        self.enfants.append(noeud_enfant)

    def afficher_polonaise(self):
        """Affiche l'expression en notation polonaise (préfixée)."""
        res = str(self.valeur)
        for enfant in self.enfants:
            res += " " + enfant.afficher_polonaise()
        return res

    def evaluer(self, variables):
        """
        Évalue l'expression symbolique pour des valeurs de variables données.
        :param variables: dict contenant les valeurs des variables (ex: {'x': 3, 'y': 2})
        :return: float
        """
        # Case 1: Le noeud est un nombre (int ou float)
        if isinstance(self.valeur, (int, float)):
            return float(self.valeur)

        # Case 2: Le noeud est une variable
        if isinstance(self.valeur, str) and not self.enfants:
            if self.valeur in variables:
                return float(variables[self.valeur])
            else:
                raise ValueError(f"La variable '{self.valeur}' n'est pas définie dans le dictionnaire.")

        # Case 3: Le noeud est un opérateur
        op = self.valeur

        if op == '+':
            return self.enfants[0].evaluer(variables) + self.enfants[1].evaluer(variables)
        elif op == '-':
            return self.enfants[0].evaluer(variables) - self.enfants[1].evaluer(variables)
        elif op == '*':
            return self.enfants[0].evaluer(variables) * self.enfants[1].evaluer(variables)
        elif op == '/':
            return self.enfants[0].evaluer(variables) / self.enfants[1].evaluer(variables)
        elif op == 'exp':
            return math.exp(self.enfants[0].evaluer(variables))
        elif op == 'sin':
            return math.sin(self.enfants[0].evaluer(variables))
        elif op == 'cos':
            return math.cos(self.enfants[0].evaluer(variables))
        elif op == 'log':
            return math.log(self.enfants[0].evaluer(variables))
        else:
            raise ValueError(f"Opérateur inconnu : {op}")

    def tracer(self, nom_variable, valeurs):
        """
        Trace la fonction correspondant à l'expression pour une variable donnée.
        :param nom_variable: str, le nom de la variable à faire varier
        :param valeurs: list de float/int
        """
        y_valeurs = []
        for val in valeurs:
            res = self.evaluer({nom_variable: val})
            y_valeurs.append(res)

        plt.plot(valeurs, y_valeurs)
        plt.xlabel(nom_variable)
        plt.ylabel("f(" + nom_variable + ")")
        plt.title("Tracé de l'expression symbolique")
        plt.grid(True)
        plt.show()