class User:
    def __init__(self, id: int, email: str, password: str) -> None:
        self.id = id
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, adict):
        return cls(
            id=adict.get('id'),
            email=adict.get('email'),
            password=adict.get('password'),
        )

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()