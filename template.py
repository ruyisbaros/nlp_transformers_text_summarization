import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s: %(name)s")

project_name = "TextSummaries"

list_of_files = [
    ".github.com/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/utils/common.py",
    "src/models/__init__.py",
    "src/models/train.py",
    "src/models/test.py",
    "src/logging/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "research/trials.ipynb",
    "app.py",
    "main.py",
    "setup.py",
    "params.yaml",
    "config/config.yaml",
    "requirements.txt",
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, file_name = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w"):
            logging.info(f"Created file: {file_path}")

    else:
        logging.info(f"File already exists: {file_path}")
