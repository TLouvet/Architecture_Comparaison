from datetime import date
from infra.db.inmemory.entities.author_inmemory import AuthorInMemory

author_db = {
    1: AuthorInMemory(
        id=1,
        first_name="Victor",
        last_name="Hugo",
        birth_date=date(1802, 2, 26),
        nationality="Français",
        death_date=date(1885, 5, 22),
        biography="Écrivain et poète français, auteur de Les Misérables.",
        books=[101, 102]
    ),
    2: AuthorInMemory(
        id=2,
        first_name="George",
        last_name="Orwell",
        birth_date=date(1903, 6, 25),
        nationality="Anglais",
        death_date=date(1950, 1, 21),
        biography="Écrivain britannique, auteur de 1984 et Animal Farm.",
        books=[103, 104]
    )
}