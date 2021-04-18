import os

from .task import Task


def test():
    task = Task()

    github_body = {
        "githaxs": {"token": os.getenv("GITHUB_TOKEN")},
        "pull_request": {"base": {"ref": "GabeL7r-patch-9"}},
        "repository": {"default_branch": "master", "full_name": "githaxs/test"},
    }

    settings = {"prettier_config": {"singleQuote": True, "semi": False}}
    result = task.execute(github_body, settings)

    print(task.fail_text)

    assert result is True
