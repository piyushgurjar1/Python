import json
expected_schema = ["name", "age", "email"]

def validate_schema(data, schema):
    missing_fields = []
    for entry in data:
        missing = []
        for field in schema:
            if field not in entry:
                missing.append(field)
        missing_fields.append(missing)
    return missing_fields

def generate_report(data, missing_fields):

    total_entries = len(data)
    print(f"Total entries: {total_entries}")
    for i, entry in enumerate(missing_fields):
        if entry:
            print(f"Missing fields: {entry}")
    
file_path = 'data.json'
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

if data is not None:
    missing_fields = validate_schema(data, expected_schema)
    generate_report(data, missing_fields)

        