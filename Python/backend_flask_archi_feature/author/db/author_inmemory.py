from datetime import date
from typing import List, Optional

class AuthorInMemory:
    def __init__(self, id: int, first_name: str, last_name: str, birth_date: date,
                 nationality: Optional[str] = None, death_date: Optional[date] = None,
                 biography: Optional[str] = None, books: Optional[List[int]] = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.nationality = nationality
        self.death_date = death_date
        self.biography = biography
        self.books = books or []