import os
def merge_files(file_names, output_file):
    try:
        all_lines = []
     
        for file_name in file_names:
            if os.path.exists(file_name):
                try:
                    with open(file_name, 'r') as file:
                        lines = file.readlines()
                        all_lines.extend(lines)  
                except Exception as e:
                    print(f"Error reading {file_name}: {e}")
            else:
                print(f"File {file_name} does not exist.")



            all_lines = list(set(all_lines))

        with open(output_file, 'w') as output:
            output.writelines(all_lines)

        print(f"Files merged successfully into {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

files = ['file1.txt', 'file2.txt', 'file3.txt']
output_file = 'merged_output.txt'
merge_files(files, output_file)
