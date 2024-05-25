# backend/app/utils/getprojecttext.py

import os

def combine_project_files(output_file='project_files.txt'):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk('.'):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"\n\n# File: {file_path}\n\n")
                        outfile.write(infile.read())
                except Exception as e:
                    print(f"Could not read file {file_path}: {e}")

if __name__ == '__main__':
    combine_project_files()
