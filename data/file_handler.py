import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'saved_data')

def write_data_to_file(filename, data):
    filepath = os.path.join(DATA_DIR, filename)
    
    with open(filepath, 'w') as file:
        json.dump(data, file)

def read_data_from_file(filename):
    filepath = os.path.join(DATA_DIR, filename)
    
    if not os.path.exists(filepath):
        return None

    with open(filepath, 'r') as file:
        return json.load(file)
