class UserRepository:
    def get_list(self, request):
        raise NotImplementedError()

    def get(self, request):
        raise NotImplementedError()

    def create(self, request):
        raise NotImplementedError()
