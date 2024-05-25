# backend/app/utils/update_comment_filename.py

import os

def update_files_with_relative_path(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(file_path, root_dir)
            
            # Verifica se a primeira linha já contém o comentário do caminho
            with open(file_path, 'r') as file:
                first_line = file.readline().strip()
            
            if first_line != f"# {relative_path}":
                # Lê todo o conteúdo do arquivo
                with open(file_path, 'r') as file:
                    content = file.readlines()
                
                # Adiciona o comentário com o caminho relativo na primeira linha
                content.insert(0, f"# {relative_path}\n")
                
                # Escreve o conteúdo de volta no arquivo
                with open(file_path, 'w') as file:
                    file.writelines(content)

if __name__ == "__main__":
    # Substitua 'seu_diretorio' pelo diretório que deseja atualizar
    root_directory = 'backend/app'
    update_files_with_relative_path(root_directory)


import os

def update_files_with_relative_path(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            relative_path = os.path.relpath(file_path, os.path.dirname(root_dir))
            
            # Verifica se a primeira linha já contém o comentário do caminho
            with open(file_path, 'r') as file:
                first_line = file.readline().strip()
            
            if first_line != f"# {relative_path}":
                # Lê todo o conteúdo do arquivo
                with open(file_path, 'r') as file:
                    content = file.readlines()
                
                # Adiciona o comentário com o caminho relativo e uma linha em branco na primeira linha
                content.insert(0, f"# {relative_path}\n\n")
                
                # Escreve o conteúdo de volta no arquivo
                with open(file_path, 'w') as file:
                    file.writelines(content)

if __name__ == "__main__":
    root_directory = 'backend'
    update_files_with_relative_path(root_directory)
