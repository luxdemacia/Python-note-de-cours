# Dans script
```└─$ python Presenter.py Je suis Boubacar
Argument reçu par se Prensenter:
-Je
-suis
-Boubacar
```
### Pour éviter cela soit on met des guillemets
```└─$ python Presenter.py "Je suis Boubacar"
Argument reçu par se Prensenter:
-Je suis Boubacar
```
### Soit combiner les arguments dans le code
Regrouper les arguments dans le programme Python en utilisant " ".join() pour reconstituer la chaîne.
        ```# Reconstituer une chaîne unique
        complete_arg = " ".join(self.args)
        print(f"- {complete_arg}")```
		