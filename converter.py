import subprocess
from pathlib import Path

path = input("Enter input path: ").strip().strip('"')
path = Path(path)

if not Path.exists(path):
    print("Path does not exist.")
    exit()

ext = input("enter desired format: ").strip().lower()

base, _ = path.stem, path.suffix
new = base + "." + ext

result = subprocess.run(["magick", path, new])

if result.returncode == 0:
    print(f"success: {new}")
else:
    print("failed")