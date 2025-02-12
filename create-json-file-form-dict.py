import json


def create_json_file_form_dict(data):
    # File name
    filename = 'data.json'

    # Writing data to JSON file
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
