import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, filename='logs', filemode = 'w', format= '[%(asctime)s]: %(name)s: %(levelname)s: %(message)s', datefmt="%Y-%m-%d %H:%M:%S") 

project_name = 'textSummarizer'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb"
    ]

for filepath in list_of_files:
    filepath = Path(filepath) # detects the system OS & accordingly convert the pathstring given in list_of_files
    filedir, filename = os.path.split(filepath) # split the file directory & file name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory:{filedir} for the {filename}')
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #check if file path is present & it contains a file that has nonzero size then it will not replace existing file with new file
        with open(filepath, "w") as f:
            pass
            logging.info(f'creating empty file: {filepath}')
    
    else:
        logging.info(f'{filename} already exists')