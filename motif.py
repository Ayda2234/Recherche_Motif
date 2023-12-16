import re
import time
import matplotlib.pyplot as plt

def rechercher_motif(texte, motif):
    debut_temps = time.time()  # Enregistrez le temps de début

    # Utilisation de re.search() pour rechercher le motif dans le texte
    resultat = re.search(motif, texte)

    fin_temps = time.time()  # Enregistrez le temps de fin
    temps_recherche = fin_temps - debut_temps

    if resultat:
        print("Motif trouvé ")
    else:
        print("Motif non trouvé dans le texte.")

    return temps_recherche

# Exemple d'utilisation avec variation de la taille du texte
motif_a_rechercher = "Strasbourg"

tailles_texte = [1000, 10000, 100000, 1000000]  # Différentes tailles de texte à tester

temps_execution = []

for taille in tailles_texte:
    texte = "Strasbourg is the capital of the Alsace region in eastern France and lies on the border with Germany, giving it a unique flavour of both countries.   It is in the Bas-Rhin department and enjoys a truly Franco-German culture having been under both French and German rule over the centuries.  Strasbourg is the home of the European Parliament which is directly elected by the European Union and the seat of several international institutions.   Historically, the city was German speaking but French is now the dominant language amongst a worldwide audience.   Following the end of the second world war, with its strategic location and cosmopolitan atmosphere,  Strasbourg was chosen to be the capital of Europe.  The city is an excellent example of reconciliation between different nations,  heralding the best of different cultures and is a bridge of unity between France and Germany.   With its diverse nature, the capital also balances the coexistence of Catholic and Protestant ideals, celebrated with its magnificent cathedral and churches." * taille

    temps_recherche = rechercher_motif(texte, motif_a_rechercher)
    temps_execution.append(temps_recherche)

    print(f"Taille du texte: {taille}, Temps de recherche: {temps_recherche} secondes\n")

# Création du graphe
plt.plot(tailles_texte, temps_execution, marker='o')
plt.title('Temps d\'exécution de la recherche en fonction de la taille des données')
plt.xlabel('Taille des données')
plt.ylabel('Temps d\'exécution (s)')
plt.show()
