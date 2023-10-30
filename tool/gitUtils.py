import sys
from colorama.ansi import Fore
import git
from git import Repo
from git import RemoteProgress
from tqdm import tqdm


class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()


def clone_repo(repo_name, repo_url, location, clone_branch = 'development'):
    print('-----------------------------------------------------')
    print(Fore.CYAN+'Starting clone ' + repo_name)
    try:
        Repo.clone_from(repo_url, location, branch=clone_branch, progress=CloneProgress())
        print('Done!'+Fore.WHITE)
    except git.GitError as e:
        print(Fore.RED)
        print(e)
        sys.exit(1)


def update_repo(repo_name, location):
    repo = Repo(location)
    origin = repo.remotes
    print(Fore.CYAN+'Starting fetching the ' + repo_name + Fore.RESET)
    for remote in origin:
        try:
            remote.fetch(progress=CloneProgress())
        except git.GitError as e:
            print(Fore.RED)
            print(e)
            sys.exit(1)
        print(Fore.CYAN+'Starting pulling the ' + repo_name + Fore.RESET)
        try:
            remote.pull(progress=CloneProgress())
        except git.GitError as e:
            print(Fore.RED)
            print(e)
            sys.exit(1)


def clean_repo(repo_name, location):
    repo = Repo(location)
    print(Fore.GREEN + "Reset the repo " + repo_name + Fore.RESET)
    try:
        repo.git.reset("--hard", "origin/development")
    except git.GitError as e:
        print(Fore.RED)
        print(e)
        sys.exit(1)
