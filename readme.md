# La Programmation Orientée Objet combinée avec la Programmation Modulaire (en Python):
Ce guide permet de comprendre, en Python, la programmation orientée objet et modulaire
qui peut être utile pour faire des scripts & faire des automatisations.


Allez dans le dossier ```/ProgrammationModlaire/```

Exécutez la commande 
```python Presenter.py```
Vous remarquerez que notre programme attend un ou des arguments!
C'est grâce à la bibliothèque ```sys``` et l'utilisation des arguments de lignes de commande via ```sys.argv```.
Donc ```sys.argv``` est la clé pour transmettre des arguments
Et  ```sys.argv[1:] ``` permet de recupérer ces arguments (en fin du code).
Maintenant, Exécutez la commande ```python Reglage.py Programme1 Programme2```.
```
→ Argument reçu et effectué par le Réglage :
	-Programme1
	-Programme2
```
## (Optionnel) Pour faire afficher un texte entier:

En exécutant la commande :
```python Presenter.py Programme1 De La Samaine```

On remarquerez à la sortie:
```
→ Argument reçu et effectué par le Réglage :
	-Programme1
	-De
	-La
	-Samaine
```
Pour éviter celà, on peut regrouper les arguments dans le programme en utilisant ```" ".join()``` pour reconstituer la chaîne (```/Reglage_Arguments_complet.py```.

On supprime la boucle for.
```
	Arguments_complet = " ".join(self.Mon_Argument)
	print(f"- {Arguments_complet}")
```

# La partie Programmation Orientée Objet

On a une poo du fait que le programme repose sur :

→ Utilisation de classes : ```Reglage```.

→ Un constructeur :	```__init__(self, Mon_argument)```

→ Encapsulation : self.Mon_argument est un attribut encapsulé dans la classe Reglage.

→ Une méthode : ```run``` qui définit le comportement de l'objet (agit sur les données).

→ Instances de classes (Objets) : ```reglage``` est créé dans la fonction ```Mis_a_jour``` en appelant le constructeur de la classe ```Reglage```


```Mis_a_jour``` est une fonction simple et non une méthode car elle n'est pas définie dans la classe.
Elle ne respecte pas non plus le ```polymorphisme``` sinon on aurait un ```même nom de méthode``` ou de ```fonction``` que la class.
On ne peut pas dire que la fonction ```Mis_a_jour``` hérite de la classe ```Reglage``` sinon on aurait:
```def Mis_a_jour(Reglage):```

```Mis_a_jour(Mon_argument):``` utilise la classe ```Reglage``` via la composition ou délégation.
Cependant, ```Mis_a_jour()``` est une ```interface``` simplifiée pour la classe ```Reglage```.

Exemple : Au lieu de demander à l'utilisateur de créer un objet Reglage manuellement, la fonction Mis_a_jour s'en charge, simplifiant le processus pour l'utilisateur final.


# A suivre...

        
		
