# Architecture par feature

Je vous ai montré en cours une architecture assez complète (et surtout complexe), qui s'inspire de ce qu'on appelle le Domain Driven Design (DDD).

Je vous propose dans ce dossier une autre architecture, par feature, beaucoup plus aplatie et également plus facile à prendre en main.

Il y a toujours autant de fichiers, mais la façon dont ils sont organisés est différente.

Là où la première architecture pense surtout "où est le code, que fait-il ?", cette architecture par feature dit plutôt "voici telle feature, et tout ce qui s'y rapporte". Si vous avez des petits projets (j'entends par là dont la complexité reste modérée), prenez plutôt l'architecture par feature.

Si vous êtes amenés à travailler sur des gros projets, il y a des chances pour que ça soit quelque chose qui se rapproche de ce que nous avons vu en cours.

Remarquez que puisqu'il s'agit d'une simple réorganisation du code, tous les concepts que nous avons vu s'appliquent toujours : DTO / Controllers / Mappers / Services / Repositories sont présents.

# Comparaison entre 2 backends en Python -> Flask vs FastAPI

Vous trouverez deux implémentations en Python, une en Flask et une en FastAPI. Celle en Flask est celle utilisée pour le cours.
L'objectif de ces implémentations et de vous montrer qu'avec une architecture de code bien pensée, on peut changer de framework sans trop d'effort.

Pour être honnête, ça m'a pris 20 minutes de faire le changement de framework (pour un framework que je n'ai absolument jamais utilisé, avec ChatGPT pour la syntaxe donc), mais plus du double pour écrire ce fichier de readme.

Prenez quelques minutes pour comparer les codes, vous verrez que le fichier main et les fichiers de controllers sont différents.
En revanche, les dossiers domain, services, infra (base de données), n'ont pas changé

Comme il y a un changement dans la lib de DTO, ça bouge également de ce côté là, en revanche cela tient d'un problème de design initial, plus particulièrement dans le fait de s'être enfermé dans un package lié à Flask.

## main.py

En Flask:

```python
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .flaskenv
load_dotenv()
app = Flask(__name__)

# Les CORS pour permettre à notre front de se connecter
CORS(app, resources={r"/*": {"origins": "*"}})

# Importer et enregistrer les blueprints des contrôleurs
from controllers.author_controller import author_bp
from controllers.user_controller import user_bp

# Enregistrer les blueprints pour chaque contrôleur
app.register_blueprint(author_bp)
app.register_blueprint(user_bp)


# Route de base pour vérifier que l'API est en ligne
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="API is live!")
```

En FastAPI:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()

app = FastAPI()

# Les CORS pour permettre à notre front de se connecter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modifier selon vos besoins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importer et enregistrer les routes des contrôleurs
from controllers.author_controller import router as author_router
from controllers.user_controller import router as user_router

app.include_router(author_router)
app.include_router(user_router)

# Route de base pour vérifier que l'API est en ligne
@app.get("/hello")
async def hello():
    return {"message": "API is live!"}
```

## Cas des DTO

Vous remarquerez que les DTO sont gérés différemment, car dans le backend flask nous avons fait le choix d'utiliser un package propre à ce framework.

Impélentation initiale pour respecter flask_expects_json:

```python
# <backend>/shared/dto/schemas/author_dto.py
author_dto = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string", "maxLength": 100},
        "last_name": {"type": "string", "maxLength": 100},
        "birth_date": {"type": "string", "format": "date"},
        "death_date": {"type": "string", "format": "date"},
        "nationality": {"type": "string", "maxLength": 100},
        "biography": {"type": "string", "maxLength": 2000},
        "books": {
            "type": "array",
            "items": {"type": "integer"},
            "uniqueItems": True
        }
    },
    "required": ["first_name", "last_name", "birth_date", "nationality"],
    "additionalProperties": False
}
```

```python
@author_bp.route('/authors', methods=['POST'])
@expects_json(author_dto_schema)
def create_author():
    dto = request.json
    author = author_mapper.to_domain(dto)
    created_author = author_service.create_author(author)
    return jsonify(author_mapper.to_external(created_author)), 201
```

Toutefois des packages plus génériques existent tels que **Pydantic**.
Notez que Flask n'a pas de support natif pour Pydantic, **MAIS** qu'il existe un package _flask-pydantic_ qui vous évite l'instanciation.

Réfléchissez donc également aux packages que vous utiliserez pendant vos conceptions, cela pourra vous permettre d'éviter d'être trop liés à un framework et devoir effectuer des changements supplémentaires.

Pour les schémas, nous sommes passés d'objets à une définition class-based:

Implémentation générique Pydantic:

```python
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional, Set

class AuthorDTO(BaseModel):
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    birth_date: str
    death_date: Optional[str] = None
    nationality: str = Field(..., max_length=100)
    biography: Optional[str] = Field(None, max_length=2000)
    books: List[int] = Field(default_factory=set)
```

Pour l'appel dans les controllers, avec Flask (implémentation possible de Pydantic):

```python
## si on utilisait pydantic avec Flask:
@author_bp.route('/authors', methods=['POST'])
def create_user():
    try:
        dto = AuthorDTO(**request.json)
        author = author_mapper.to_domain(dto)
        created_author = author_service.create_author(author)
        return jsonify(author_mapper.to_external(created_author)), 201
    except ValidationError as e:
        return jsonify(e.errors()), 400


## si on utilisait pydantic avec Flask et flask-pydantic
@author_bp.route('/authors', methods=['POST'])
@validate()
def create_user(dto: AuthorDTO):
    author = author_mapper.to_domain(dto)
    created_author = author_service.create_author(author)
    return jsonify(author_mapper.to_external(created_author)), 201
```

Avec FastAPI:

```python
@router.post("/authors", status_code=status.HTTP_201_CREATED)
async def create_author(dto: AuthorDTO):
    author = author_mapper.to_domain(dto.dict())
    created_author = author_service.create_author(author)
    return author_mapper.to_external(created_author)
```

Les changements sur les mappers sont minimes, avec du typage et l'instanciation d'un DTO sur to_external:

```python

#<backend>/shared/dto/mappers/author_dto_mapper.py
from datetime import datetime
from domain.kernel.Mapper import BaseMapper
from domain.entities.Author import Author

class AuthorDTOMapper(BaseMapper[Author, dict]):
    def to_domain(self, dto: dict, author_id: int = 0) -> Author:
        """Transforme un dictionnaire DTO en objet domaine Author."""
        return Author.create(
            id=author_id,
            first_name=dto["first_name"],
            last_name=dto["last_name"],
            birth_date=datetime.strptime(dto["birth_date"], "%Y-%m-%d").date(),
            nationality=dto.get("nationality"),
            death_date=datetime.strptime(dto["death_date"], "%Y-%m-%d").date() if dto.get("death_date") else None,
            biography=dto.get("biography"),
            books=dto.get("books", [])
        )

    def to_external(self, author: Author) -> dict:
        """Transforme un objet domaine Author en dictionnaire DTO."""
        return {
            "id": author.id,
            "first_name": author.first_name,
            "last_name": author.last_name,
            "birth_date": author.birth_date.isoformat(),
            "nationality": author.nationality,
            "death_date": author.death_date.isoformat() if author.death_date else None,
            "biography": author.biography,
            "books": author.books
        }
```

Une fois qu'on a utilisé Pydantic, notez qu'il y a très peu d'évolution (encore une fois on aurait pu se passer de ça si on avait harmonisé nos packages de validation dès la conception initiale):

```python
from datetime import datetime
from domain.kernel.Mapper import BaseMapper
from domain.entities.Author import Author
from shared.dto.schemas.author_dto import AuthorDTO

class AuthorDTOMapper(BaseMapper[Author, AuthorDTO]):
    def to_domain(self, dto: AuthorDTO, author_id: int = 0) -> Author:
        """Transforme un dictionnaire DTO en objet domaine Author."""
        return Author.create(
            id=author_id,
            first_name=dto["first_name"],
            last_name=dto["last_name"],
            birth_date=datetime.strptime(dto["birth_date"], "%Y-%m-%d").date(),
            nationality=dto.get("nationality"),
            death_date=datetime.strptime(dto["death_date"], "%Y-%m-%d").date() if dto.get("death_date") else None,
            biography=dto.get("biography"),
            books=dto.get("books", [])
        )

    def to_external(self, author: Author) -> AuthorDTO:
        """Transforme un objet domaine Author en dictionnaire DTO."""
        return AuthorDTO(
            first_name=author.first_name,
            last_name=author.last_name,
            birth_date=author.birth_date.isoformat(),
            nationality=author.nationality,
            death_date=author.death_date.isoformat() if author.death_date else None,
            biography=author.biography,
            books=author.books
        )
```
