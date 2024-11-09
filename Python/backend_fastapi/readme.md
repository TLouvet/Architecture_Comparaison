# Bibliothèque online - Backend FastAPI

Installer les requirements avec pip install -r requirements.txt

Lancer l'application avec `uvicorn main:app --reload`

## Quelles sont les différences avec le backend Flask ?

- La configuration des CORS directement embarquée dans FastAPI, syntaxe d'enregistrement des controllers légèrement différente
- Léger changement dans la définition des routes des controllers
- Les DTO, mappers, import (voir en dessous pourquoi cela est lié à un problème de design initial)

## Changements liés à des libs (DTO)

- Notez bien que si nous avions utilisé pydantic dans notre backend Flask initial, aucun des changements ci-dessous ne serait nécessaire

- J'ai fait le choix d'utiliser pydantic, qui n'est pas lié à Flask contrairement à flask_expects_json
- Par conséquent, les DTO ont changé pour être class-based, et la validation a changé également pour refléter le package pydantic
- Les controllers appellent le type directement dans le type hint
- Les modules n'importent plus les DTO puisque les classes sont automatiquement instanciées
- Les mappers prennent en compte le type DTO créé et la fonction to_external a été modifiée pour instancier une classe plutôt que de retourner un objet

## Ce qui n'a pas changé

- Le dossier domain
- Le dossier services
- Le dossier infra (donc tout ce qui est lié à la Base de données)

## Résultat

En moins de 20 minutes, avec ChatGPT, j'ai remplacé mon framework Flask par FastAPI, alors que j'en ai jamais fait.
L'architecture modulaire me permet de faire évoluer mon app sans pour autant tout modifier

Temps de travail:

- Prompter GPT en décrivant le besoin et l'archi, 1 minute
- Remplacer les fichiers par les réponses: 5 minutes
- Débugger les incohérences et erreurs de lib: 10 minutes
