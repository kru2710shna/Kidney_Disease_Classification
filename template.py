import os
from pathlib import Path
import logging


# Logging String 
logging.basicConfig(level=logging.INFO , format='[%(asctime)s]:%(message)s:')

# Project name
project_name = 'cnnClassifier'

# List of files and folder
list_of_folder = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_folder:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)
    
    # Create directories if they do not exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory; {filedir} for the file: {filename}")
    
    # Create empty files if they do not exist or are empty
    if (not file_path.exists()) or (file_path.stat().st_size == 0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"Creating Empty file: {file_path}")
    else:
        logging.info(f"{file_path} already exists.") 