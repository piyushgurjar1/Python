from fetch_data import fetch_data
from process_data import process_data
from reports_results import report_results

input_file = 'file1.txt'
output_file = 'file2.txt'

data = fetch_data(input_file)
if data:
    processed_data = process_data(data)
    report_results(processed_data, output_file)