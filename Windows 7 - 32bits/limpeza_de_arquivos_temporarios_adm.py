import os
import shutil
import traceback

def clean_temp_folder(path):

    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  
                print(f'Removido: {file_path}')
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  
                print(f'Removido: {file_path}')
        except Exception as e:
            print(f'Falha ao excluir {file_path}. Motivo: {e}')
            traceback.print_exc()

temp_path = r'C:\Windows\Temp'
clean_temp_folder(temp_path)