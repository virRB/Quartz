from pathlib import Path
import shutil
import sys
import subprocess
import importlib.util

BASE = Path.cwd()
MAIN = Path(__file__).resolve().parent
TEMPLATE_DIR = MAIN / "template"
Qversion = "Quartz v1.2"

def build_project(name):
    target = BASE / name

    if target.exists():
        print(f"ERROR: Project already exists -> {target}")
        return

    if not TEMPLATE_DIR.exists():
        print(f"ERROR: Template folder missing -> {TEMPLATE_DIR}")
        return

    shutil.copytree(TEMPLATE_DIR, target)

    print(f"Built Quartz project: {name}")

def load_module(path):
    spec = importlib.util.spec_from_file_location("Quartz", str(path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_project():
    cwd = Path.cwd()
    quartz_file = cwd / "Quartz.py"

    if not quartz_file.exists():
        print("ERROR: Quartz.py not found in current directory")
        return

    print("Running Quartz.py...")

    subprocess.run(["py", str(quartz_file)], cwd=cwd)


def main():
    args = sys.argv[1:]

    if not args:
        print(Qversion)
        return

    cmd = args[0]

    if cmd == "build":
        if len(args) < 2:
            print("Usage: qz build <name>")
            return
        build_project(args[1])

    elif cmd == "run":
        run_project()
    elif cmd == "version":
        print(Qversion)
    elif cmd == "help":
        print("Help:\nqz build <projectname> -> creates a new Quartz project with that name\nqz run -> runs the project in the current directory\nqz version -> displays your current installed version of Quartz\nqz help -> displays help text for Quartz")
    elif cmd == "dbgr":
        c_dir = Path.cwd()
        parser = c_dir / "Quartz.py"
        if parser.exists():
            quartz = load_module(parser)
            quartz.debugger()
            quartz.run()
        else:
            print("ERROR: cannot find parser file")
    else:
        print(f"ERROR: Unknown command -> {cmd}")


if __name__ == "__main__":
    main()
