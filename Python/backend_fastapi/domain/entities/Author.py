from datetime import date
from typing import List, Optional

class Author:
    ALLOWED_NATIONALITIES = {"Français", "Anglais", "Américain", "Espagnol", "Allemand"}

    def __init__(self, id: int, first_name: str, last_name: str, birth_date: date, nationality: Optional[str] = None,
                 death_date: Optional[date] = None, biography: Optional[str] = None, books: Optional[List[int]] = None):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date
        self._nationality = nationality
        self._death_date = death_date
        self._biography = biography
        self._books = books or []

    @staticmethod
    def create(id: int, first_name: str, last_name: str, birth_date: date, nationality: Optional[str] = None,
               death_date: Optional[date] = None, biography: Optional[str] = None, books: Optional[List[int]] = None):

        if nationality and nationality not in Author.ALLOWED_NATIONALITIES:
            raise ValueError(f"Nationalité '{nationality}' non reconnue. Les nationalités acceptées sont : {Author.ALLOWED_NATIONALITIES}")
        
        if death_date and birth_date >= death_date:
            raise ValueError("La date de naissance doit être antérieure à la date de décès.")
        
        return Author(id, first_name, last_name, birth_date, nationality, death_date, biography, books)

    @property
    def id(self) -> int:
        return self._id

    @property
    def first_name(self) -> str:
        return self._first_name
    
    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def birth_date(self) -> date:
        return self._birth_date

    @property
    def nationality(self) -> Optional[str]:
        return self._nationality

    @property
    def death_date(self) -> Optional[date]:
        return self._death_date

    @property
    def biography(self) -> Optional[str]:
        return self._biography
    
    @property
    def books(self) -> List[int]:
        return self._books
    
