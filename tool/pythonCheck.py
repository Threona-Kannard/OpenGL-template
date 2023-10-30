import sys
import subprocess
from importlib import import_module


def python_version():
    return sys.version_info[0]


def is_module_exist(module_name):
    try:
        import_module(module_name)
        return True
    except:
        return False


def install_module(module_name):
    print(f"Start downloading the module {module_name}")
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", module_name])
        print(f"Download completed!!!")
    except subprocess.CalledProcessError as e:
        print(e)
        sys.exit(1)
