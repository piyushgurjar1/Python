def fetch_data(file_path):
        with open(file_path, 'r') as file:
            data = file.readlines()
        return data
