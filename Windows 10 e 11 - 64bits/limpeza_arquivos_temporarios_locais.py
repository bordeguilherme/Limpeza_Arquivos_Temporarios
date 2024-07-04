import os
import shutil

def limpar_temp():
  
    temp_path = os.environ['TEMP']
    

    for item in os.listdir(temp_path):
        item_path = os.path.join(temp_path, item)
        try:

            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
            print(f'Removido: {item_path}')
        except Exception as e:
            print(f'Erro ao remover {item_path}: {e}')


limpar_temp()
