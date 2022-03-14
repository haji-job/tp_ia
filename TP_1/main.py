import time
from noeud import Noeud
from exploration import Exploration
from taquin.probleme import Probleme
from taquin.etat import Etat


###############################################
# Taquin
###############################################

plateau = [[1,2,3],[4,5,0],[6,7,8]]
but = [[1,2,3],[4,5,6],[7,8,0]]

etat_cible = Etat(but)

etat_initial = Etat(plateau)
# OU
# etat_initial = Probleme.melanger(etat_cible)

probleme = Probleme(etat_initial=etat_initial, etat_final=etat_cible)

# Dijkstra
fonction_score = lambda noeud: noeud.g

###############################################
# Exploration (générique)
###############################################

exploration = Exploration(probleme=probleme, critere=fonction_score)
temps_debut = time.clock()
chemin = exploration.explorer()
temps_fin = time.clock()

###############################################
# Résultat
###############################################
print("=====================================================")
etapes = -1
print("État initial :\t" + str(probleme.etat_initial))
if len(chemin) > 0:
    last = None
    for node in chemin:
        print(node.action)
        node.etat.afficher()
        time.sleep(0.2)
        last = node
        etapes += 1
        print(last)
    print("État final :\t\t" + str(last.etat))
    print("Coût total :\t\t" + str(last.g))
else:
    print("But non atteignable")

print("Nb de noeuds explorés :" + str(exploration.n_explores))
print("Nombre d'étapes: " + str(etapes))
print("Durée de l'exploration: " + str(temps_fin - temps_debut) + " second(s)") 
