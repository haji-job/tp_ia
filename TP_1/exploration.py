import collections
import sys
from noeud import *

class Exploration:
    """
    Algorithme d'exploration
    - probleme : Problème formalisé à résoudre
    - critere : fonction qui associe un noeud à un score, le plus faible étant le meilleur
    - open : collection de noeuds connus mais pas encore explorés
    - close : collection de noeuds déjà explorés
    - n_explores : nombre de noeuds explorés (utile pour les statistiques à la fin)
    """

    def __init__(self, probleme, critere):
        self.probleme = probleme
        self.critere = critere
        self.open = dict()
        self.close = dict()
        self.n_explores = 0

    def piocher(self):
        """
        Renvoie un nouveau noeud à explorer
        """
        # À implémenter
        return None

    def mettre_a_jour_arbre(self, nouveaux_noeuds):
        """
        Met à jour l'arbre d'exploration avec un nouveau noeud
        """
        # À implémenter

    def explorer(self):
        """
        Explore un espace d'état et retourne le chemin trouvé,
        éventuellement None si aucun chemin n'est trouvé
        """
        # À implémenter
        return None