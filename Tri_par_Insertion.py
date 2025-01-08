def tri_par_insertion(Tab):
    # On commence du deuxième élément jusqu’au dernier
    for i in range(1, len(Tab)):
        cle = Tab[i]  # L'élément à insérer
        print("La valeur de i vaut:",i)
        j = i - 1  #   i - 1 correspond à l'index du dernier élément de la partie triée, qui est juste avant l'élément que nous voulons insérer.

        # Déplacer les éléments triés qui sont plus grands que la clé
        while j >= 0 and cle < Tab[j]:
            Tab[j + 1] = Tab[j]  # Déplacement vers la droite
            j -= 1  # On continue à regarder vers la gauche

        # Insérer la clé à sa position correcte
        Tab[j + 1] = cle

# Exemple
Tab = [64, 25, 12, 22, 11]
tri_par_insertion(Tab)
print("Tableau trié:")
print(Tab) 
