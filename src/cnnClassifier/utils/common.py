# Importing required libraries
import os  # For creating directories and file operations
from box.exceptions import BoxValueError  # To handle empty or invalid ConfigBox usage
import yaml  # For reading and parsing YAML files
from cnnClassifier import logger  # Custom logger from your project
import json  # For reading/writing JSON files
import joblib  # For saving/loading binary files (e.g., ML models)
from ensure import ensure_annotations  # To enforce type annotations at runtime
from box import ConfigBox  # Allows dict-like access via dot notation
from pathlib import Path  # For handling file paths in an object-oriented way
from typing import Any  # For generic typing
import base64  # For encoding/decoding images to/from base64

#Function: read_yaml

@ensure_annotations  # Enforces type hints at runtime
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    # Tries to read a YAML file and convert it into a ConfigBox (dot-access dict)

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load YAML file into a Python dict
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Log success
            return ConfigBox(content)  # Return as ConfigBox for dot-access
    except BoxValueError:
        raise ValueError("yaml file is empty")  # Raise error if YAML file has no content
    except Exception as e:
        raise e  # Raise any other unexpected error
    
#Function: create_directories

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    # Create directories listed in the input list

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Create the directory if it doesn't exist
        if verbose:
            logger.info(f"created directory at: {path}")  # Log each created directory

#Function: save_json
@ensure_annotations
def save_json(path: Path, data: dict):
    # Save a dictionary to a JSON file

    with open(path, "w") as f:
        json.dump(data, f, indent=4)  # Write dict to JSON with indentation

    logger.info(f"json file saved at: {path}")  # Log the saved file path

#Function: load_json
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    # Load data from a JSON file and return it as a ConfigBox

    with open(path) as f:
        content = json.load(f)  # Read JSON into a Python dict

    logger.info(f"json file loaded succesfully from: {path}")  # Log the read file path
    return ConfigBox(content)  # Return as ConfigBox for dot-access
#Function: save_bin
@ensure_annotations
def save_bin(data: Any, path: Path):
    # Save any Python object (e.g., model) to a binary file using joblib

    joblib.dump(value=data, filename=path)  # Save the data to a .pkl file
    logger.info(f"binary file saved at: {path}")  # Log the saved path

#Function: load_bin
@ensure_annotations
def load_bin(path: Path) -> Any:
    # Load a binary file and return the object

    data = joblib.load(path)  # Load the binary object from file
    logger.info(f"binary file loaded from: {path}")  # Log the loaded path
    return data  # Return the object

#Function: get_size
@ensure_annotations
def get_size(path: Path) -> str:
    # Return the file size in kilobytes as a string

    size_in_kb = round(os.path.getsize(path)/1024)  # Get file size in KB
    return f"~ {size_in_kb} KB"  # Return as formatted string

#Function: decodeImage
def decodeImage(imgstring, fileName):
    # Decode a base64 string and save it as an image file

    imgdata = base64.b64decode(imgstring)  # Decode the base64 image string to bytes
    with open(fileName, 'wb') as f:
        f.write(imgdata)  # Write image bytes to a file
        f.close()  # Close file (optional here, as 'with' handles it)

#Function: encodeImageIntoBase64
def encodeImageIntoBase64(croppedImagePath):
    # Read an image file and encode it into a base64 string

    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())  # Read image bytes and encode to base64