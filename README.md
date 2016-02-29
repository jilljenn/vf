# Générateur d'exercices Vrai/Faux

## Prérequis

- Python 3

## Essayer

Les planches d'exercices sont dans un format TXT, à raison d'un exercice par ligne. La ligne doit se terminer par `VRAI` ou `FAUX` selon la validité de l'assertion.

    $2 + 2 = 5$. FAUX
    $6 \times 7 = 42$. VRAI
    L'ornithorynque est un mammifère. VRAI
    $\displaystyle \forall \lambda \in \mathbb{C} \setminus \mathbb{R}, \int_{-\infty}^\infty \frac{dx}{x - \lambda} = i \pi \cdot \textrm{sgn}(\Im(\lambda)).$ VRAI
    ...

Une fois les fichiers TXT tapés, il suffit de faire :

    python3 vf.py

pour créer toutes les pages, puis taper :

    python3 -m http.server

et aller à http://localhost:8000 pour vérifier que les pages conviennent bien.

Pour fermer le serveur, il suffit de taper `Ctrl-C`.

## Configuration

Il est également possible de modifier la description en page d'accueil en modifiant le fichier `conf.py`.
