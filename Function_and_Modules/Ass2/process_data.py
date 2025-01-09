def process_data(data):
    processed_data = "" 
    for line in data:
        processed_data += line.upper()  
    return processed_data