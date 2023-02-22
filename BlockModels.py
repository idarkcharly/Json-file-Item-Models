# @Author : Charly1307
# Version : 1.0
# Loop to be stopped manual
import json
import os

print("================welcome================\n")
print("Json file generator for Block Models\n")
# You can change the path HERE
print("EXAMPLE: C:\\Users\\carlos\\Desktop\\Guardar\\")
path = str(input("Insert the PATH directory: \n"))
file_path = os.path.join(path)

mod_id = str(input("Insert the modid: \n"))

while True:
    block_id = str(input("Insert the block id: \n"))
    # Python dictionary
    block_models = {
        "parent": "block/cube_all",
        "textures": {
            "all": ""

        }
    }

    block_models["textures"]['all'] = mod_id + ':block/' + block_id
    # Serializing json
    json_object = json.dumps(block_models, indent=4)
    # Generate json file
    with open(file_path + block_id+'.json', "w") as outfile:
        outfile.write(json_object)
        print("=======SUCCESS=======\n")
