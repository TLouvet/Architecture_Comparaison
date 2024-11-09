class UserInMemory:
    def __init__(self, id: int, email: str, password: str, role: str, first_name: str, last_name: str):
        self.id = id
        self.email = email
        self.password = password
        self.role = role 
        self.first_name = first_name
        self.last_name = last_name