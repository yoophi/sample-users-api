from flask import current_app
from werkzeug.local import LocalProxy

from app.repositories.mem import MemRepo
from app.repositories.sqla import SqlaRepo

repo_mappings = {
    'MYSQL': SqlaRepo,
    'MEMORY': MemRepo,
}


def _get_repo():
    cls = repo_mappings.get(current_app.config.get("REPOSITORY"), MemRepo)

    if cls is MemRepo:
        if not getattr(_get_repo, 'mem_repo', None):
            _get_repo.mem_repo = cls({})

        return _get_repo.mem_repo

    return cls()


current_repo = LocalProxy(_get_repo)
