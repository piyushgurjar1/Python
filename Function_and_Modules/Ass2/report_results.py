def report_results(data, output_path):
        with open(output_path, 'w') as file:
            for line in data:
                file.write(line + '\n')
        print(f"Results have been written to {output_path}")
