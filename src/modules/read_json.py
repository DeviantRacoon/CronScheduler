import json
import os

def read_json_file(file_name):
    """
    Reads the JSON file and returns its contents as a Python object.

    :param file_name: The name of the JSON file to read.
    :type file_name: str
    :return: The contents of the JSON file as a Python object.
    """
    try:
        file_path = os.path.join(os.path.abspath('jsons'), file_name)
        
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            
        # Assuming your JSON structure has a top-level list or dictionary
        return json_data  # Return the entire JSON structure

    except Exception as e:
        print("Error reading JSON file:", e)
        return []  # Return an empty list if there's an error

if __name__ == "__main__":
    data = read_json_file('endpoints.json')
    
    for item in data:
        print("Name:", item.get('name'))
