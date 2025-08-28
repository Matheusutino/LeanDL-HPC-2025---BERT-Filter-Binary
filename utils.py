import os
import json

def save_dict_to_json(data: dict, path: str):
    """
    Save a dictionary in JSON format.
    
    Args:
        data (dict): Dictionary to be saved.
        path (str): Full file path (e.g., 'results/classification_report.json').
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"✅ Dictionary saved at: {path}")


def create_directory(path: str):
    """
    Create a directory at the specified path if it does not exist.

    Args:
        path (str): The directory path to be created.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory '{path}' created successfully!")
    else:
        print(f"Directory '{path}' already exists.")
