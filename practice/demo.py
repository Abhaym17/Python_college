# this is a [program of delete folder if folder have file than also delete them first]

import os 
folder_path = "Demo"
if os.path.isdir(folder_path):
    for fn in os.listdir(folder_path) : 
        filepath = os.path.join(folder_path,fn)
        if os.path.isfile(filepath) :
            os.remove(filepath)
            print(fn, "file was deleted")
        
    os.rmdir(folder_path)