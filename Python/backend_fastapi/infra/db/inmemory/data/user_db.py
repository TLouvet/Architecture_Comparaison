from infra.db.inmemory.entities.user_inmemory import UserInMemory

# bien évidemment, dans un monde bien fait, les mots de passe ne sont pas en clair dans la BDD :)
user_db = {
    1: UserInMemory(id=1, email="admin@example.com", password="admin123", role="admin", first_name="Admin", last_name="User"),
    2: UserInMemory(id=2, email="reader@example.com", password="reader123", role="reader", first_name="Reader", last_name="User")
}