from git import Repo
from git import RemoteProgress
from tqdm import tqdm
import json

class CloneProgress(RemoteProgress):
    def __init__(self):
        super().__init__()
        self.pbar = tqdm()

    def update(self, op_code, cur_count, max_count=None, message=''):
        self.pbar.total = max_count
        self.pbar.n = cur_count
        self.pbar.refresh()

def main():
    # Read the file contain external repo
    file = open("external.json")
    data = json.load(file)

    for lib in data["external_lib"]:
        repo_name = lib["repo_name"] 
        repo_url = lib["repo_url"]
        clone_location = lib["clone_location"]
        Repo.clone_from(repo_url,clone_location, progress=CloneProgress())

    file.close()

main()

