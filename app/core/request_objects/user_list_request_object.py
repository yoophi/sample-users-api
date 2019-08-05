class UserListRequestObject(object):
    @classmethod
    def from_dict(cls, adict):
        return cls()


class UserCreateRequestObject:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, adict):
        return cls(**adict)
