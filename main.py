# Par Antoine Patino Conde
# Le 15 Septembre 2022
# TP1; compteur de mots
def word_count(string): # Definition dae la fonction word_counter
    words = string.split(" ") # On defini un mot comme l'oppose des espaces
    return len (words) # On veut que la valeur du word counter soit retouner a nous

chaine =input(" Ecrivez votre phrase ") # Inscrit une phrase


print(word_count(chaine)) # Le programme va compter le nombre de mots ans la chaine que tu as inscrit






