import os

def create_folder(folder_name):
    if os.path.exists("Desktop/"+folder_name) == False:
        os.chdir("Desktop/")
        os.mkdir(folder_name)
    else:
        print("Ya tiene la carpeta")