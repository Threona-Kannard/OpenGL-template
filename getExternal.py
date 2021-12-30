import tool.gitUtils as git
from colorama import Fore
import tool.pythonCheck as pc
import os
import sys
import json
from pathlib import Path

required_module = {
    'colorama': 'colorama',
    'gitpython': 'git',
    'tqdm': 'tqdm'
}

try:
    assert(pc.python_version() == 3), "Python version required at least 3.0"
    print("Python version: ", sys.version)
except Exception as err:
    print(err)
    input("Press the Enter to continue")
    sys.exit(1)

print('-----------------------------------------------------')
for module, module_name in required_module.items():
    print(f"Checking the module {module}")
    if pc.is_module_exist(module_name) == False:
        pc.install_module(module)
    else:
        print(
            f"Module {module} has been installed!!!")
    print('-----------------------------------------------------')


# Read the file contain external repo
file = Path("./external.json")

try:
    assert(file.is_file()), Fore.RED+f'The file {file.name} does not exist!'
except Exception as err:
    print(err)
    input('Press Enter to continue')
    sys.exit(1)

with open(file, 'r') as repo_data:
    data = json.load(repo_data)
for lib in data["external_lib"]:
    repo_name = lib["repo_name"]
    repo_url = lib["repo_url"]
    clone_location = lib["clone_location"]
    if os.path.isdir(clone_location):
        print(Fore.MAGENTA +
              f"The folder {repo_name} has been existed" + Fore.RESET)
    else:
        git.clone_repo(repo_name, repo_url, clone_location)
print('-----------------------------------------------------')