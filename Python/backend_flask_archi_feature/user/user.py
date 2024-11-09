class User:
    VALID_ROLES = ['admin', 'reader']

    def __init__(self, id: int, email: str, role: str, first_name: str, last_name: str):
        self.id = id
        self.email = email
        self.role = role
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create(id: int, email: str, role: str, first_name: str, last_name: str): 
        if role not in User.VALID_ROLES:
            raise ValueError(f"Role '{role}' not recognized. Valid roles are: {User.VALID_ROLES}")

        return User(id, email, role, first_name, last_name)