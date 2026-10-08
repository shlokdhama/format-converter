import subprocess
import os

path = input("Enter input path: ").strip().strip('"')

if not os.path.exists(path):
    print("Path does not exist.")
    exit()

ext = input("Enter desired format: ").strip().lower()

base, _ = os.path.splitext(path)
new = base + "." + ext

result = subprocess.run(["magick", path, new])

if result.returncode == 0:
    print(f"Success: {new}")
else:
    print("Failed")