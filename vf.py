import json
import os
import re
from conf import DESCRIPTION
from string import Template

def convert(filename):
    """Convertit un V/F au format TXT en JSON.
    Chaque ligne du fichier TXT doit contenir une ligne par question, et finir par VRAI ou FAUX selon la réponse."""

    raw_code = open('data/%s.txt' % filename).read()
    # La regexp suivante récupère énoncé et réponse d'une ligne
    pattern = re.compile('^((?:.\n?)+?) (VRAI|FAUX) *$', re.MULTILINE)

    exercises = []
    for match in pattern.finditer(raw_code):  # Tant que la regexp s'applique, ligne par ligne
        statement, answer = match.groups()
        exercises.append(dict(statement=statement, answer=answer == 'VRAI'))

    json_path = 'data/%s.json' % filename
    if not os.path.exists(json_path) or input('Le fichier %s existe. Remplacer ? [o/n] ' % json_path) == 'o':
        with open(json_path, 'w') as f:
            f.write(json.dumps(exercises))  # Création du fichier JSON à partir du TXT

    with open('base.html') as f:  # On ouvre le template de page
        html = Template(f.read()).substitute(description='', filename=filename)  # Génère le code HTML à partir du template base.html en remplaçant les variables $description et surtout $filename

    html_path = '%s.html' % filename
    if not os.path.exists(html_path) or input('Le fichier %s existe. Remplacer ? [o/n] ' % html_path) == 'o':
        with open(html_path, 'w') as f:
            f.write(html)  # Écrit ce code HTML dans la page correspondante

if __name__ == '__main__':
    for filename in os.listdir('data'):  # Pour chaque fichier dans data
        if re.match('(.*).txt', filename):  # Si c'est un fichier TXT
            convert(filename[:-4])  # On crée les fichiers JSON puis HTML correspondants

    # Création de la page d'accueil
    with open('base.html') as f:
        html = Template(f.read()).substitute(description=DESCRIPTION, filename='')
    with open('index.html', 'w') as f:
        f.write(html)
