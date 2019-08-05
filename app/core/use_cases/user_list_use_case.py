from app.core.response_objects import ResponseSuccess, ResponseFailure


class UserListUseCase(object):
    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        try:
            users = self.repo.list()
            return ResponseSuccess(users)
        except Exception as exc:
            return ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc))
            )


class UserUseCase:
    def __init__(self, repo=None):
        self.repo = repo

    def get_list(self):
        try:
            users = self.repo.list()
            return users
        except Exception as exc:
            raise exc

    def create(self, request):
        pass
