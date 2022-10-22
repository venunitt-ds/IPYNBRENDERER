import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter project name:")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

# list of fiels
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
]

for file_name_it in list_of_files:
    file_path = Path(file_name_it)
    file_dir, file_name = os.path.split(Path(file_path))
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory at: {file_dir} for file: {file_name}")
    
    if (not os.path.exists(file_path) or os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating new file: {file_name} at path: {file_path}")
    else:
        logging.info(f"File is already present at: {file_path}")
