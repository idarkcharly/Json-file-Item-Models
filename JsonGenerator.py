# @Author : Charly1307
# Version : 1.0

import json
import os

# Change the path
file_path = os.path.join('/home/carlos/Escritorio/')

mod_id = str(input("Ingresa el modid: \n"))
item_id = str(input("Ingresa el id del item: \n"))

# Python dictionary
item_models = {
    "parent": "item/generated",
    "textures": {
        "layer0": ""
    }
}

# Insert the variables
item_models["textures"]['layer0'] = mod_id + ':item/' + item_id

# Serializing json
json_object = json.dumps(item_models, indent=4)

# Generate json file
with open(file_path + item_id+'.json', "w") as outfile:
    outfile.write(json_object)
