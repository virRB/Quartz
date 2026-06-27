import shutil
from pathlib import Path
import winreg

BASE = Path(__file__).resolve().parent
TEMP = BASE / "Quartz"

HOME = Path.home()
DEST = HOME / "Quartz"


def add_to_path(new_path: str):
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_READ | winreg.KEY_WRITE
    )

    try:
        current_path, _ = winreg.QueryValueEx(key, "Path")
    except FileNotFoundError:
        current_path = ""

    if new_path in current_path:
        print("Already in PATH")
        return

    updated_path = current_path + ";" + new_path if current_path else new_path

    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, updated_path)

    print("PATH updated ✔")
    print("Restart terminal to use qz")


choice = input("Install Quartz? (y/n) > ")

if choice.lower() == "y":
    print(f"Installing Quartz in {DEST}")

    if DEST.exists():
        print("Quartz is already installed on this system.")
        input("Press Enter to exit...")
    else:
        shutil.copytree(TEMP, DEST)
        print(f"Quartz has been installed to {DEST}!")

        itp = input("Register Quartz in PATH? (y/n) > ")

        if itp.lower() == "y":
            add_to_path(str(DEST))
            input("> ")
        else:
            print("Skipping PATH registration.")

else:
    print("Ending...")