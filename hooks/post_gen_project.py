import json
import os
from pathlib import Path
import shutil
import subprocess
from subprocess import PIPE


PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
GITHUB_URL = "git@github.com:{{ cookiecutter.git_org_name }}/{}.git".format


def normalize_namespace_path(package_namespace: str) -> None:
    if "." in package_namespace:
        module_dir = package_namespace.replace(".", os.sep)
        old_dir = package_namespace
        new_dir = module_dir
        shutil.move(old_dir, new_dir)


def create_git_repo(package_name: str) -> None:
    if Path(".git").exists():
        print("[WARNING]: The .git directory already exists.")
        return

    subprocess.run(
        ["git", "init"],
        check=True,
        cwd=PROJECT_DIRECTORY,
        stdout=PIPE,
        stderr=PIPE,
    )
    subprocess.run(
        ["git", "remote", "add", "origin", GITHUB_URL(package_name)],
        check=True,
        cwd=PROJECT_DIRECTORY,
    )


def main() -> None:
    context = json.loads("""{{ cookiecutter | jsonify }}""")
    create_git_repo(context["git_repo_name"])
    normalize_namespace_path(context["package_namespace"])


if __name__ == "__main__":
    main()
