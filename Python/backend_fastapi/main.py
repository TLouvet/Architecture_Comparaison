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