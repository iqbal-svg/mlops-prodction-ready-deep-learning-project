# Import necessary libraries
import os                        # For file system operations like checking existence, creating directories, etc.
from pathlib import Path         # For handling file paths in a cleaner, cross-platform way
import logging                   # For displaying messages about what's happening

# Configure logging to show messages with timestamps
logging.basicConfig(
    level=logging.INFO,          # Set logging level to INFO (so it shows info messages)
    format='[%(asctime)s]: %(message)s:'  # Define the format of the log messages
)

# Set your project name (used to dynamically generate folder structure)
project_name = "cnnClassifier"

# Define a list of all files and folders your project should contain
# The `f"..."` strings dynamically insert the project name in the correct place
list_of_files = [
    f"src/{project_name}/__init__.py",                            # base package
    f"src/{project_name}/components/__init__.py",                # submodule: components
    f"src/{project_name}/utils/__init__.py",                     # submodule: utils
    f"src/{project_name}/config/__init__.py",                    # submodule: config
    f"src/{project_name}/config/configuration.py",              # actual configuration logic
    f"src/{project_name}/pipeline/__init__.py",                  # submodule: pipeline
    f"src/{project_name}/entity/__init__.py",                    # submodule: entity
    f"src/{project_name}/constants/__init__.py",                 # submodule: constants
    "config/config.yaml",                                        # YAML file for configuration
    "params.yaml",                                               # YAML file for hyperparameters
    "dvc.yaml",                                                  # DVC config file for data versioning
    "requirements.txt",                                          # Python package dependencies
    "setup.py",                                                  # Project installation config
    "research/trials.ipynb",                                     # Jupyter notebook for experimentation
    "templates/index.html"                                       # HTML template file
]

# Loop through each file path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to a Path object (for consistency)
    filedir, filename = os.path.split(filepath)  # Split into directory and filename

    # Create the directory if it's not empty and doesn't already exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Recursively create directories
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:  # Open file in write mode (creates if not exists)
            pass                        # Don't write anything (create empty file)
        logging.info(f"Creating empty file: {filepath}")

    # If the file already exists and is not empty, log that it's already there
    else:
        logging.info(f"{filename} already exists")