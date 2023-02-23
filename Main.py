# @Author : Charly1307
# Version : 1.0
# Stopped manual
import os
import json

# IMPORTANT, CHANGE PATH AND MOD_ID!
PATH = os.path.join("C:/Users/carlos/Desktop/JsonFiles/")
MOD_ID = "decorock"

# JSON FORMAT / PYTHON DICTIONARY
ITEM_MODEL = {
    "parent": "item/generated",
    "textures": {
        "layer0": ""
    }
}
BLOCK_MODEL = {
    "parent": "block/cube_all",
    "textures": {
        "all": ""

    }
}
BLOCKSTATES = {
    "variants": {
        "": {"model": ""}
    }
}

BLOCK_ITEM = {
    "parent": "",
}


def CreateItem():
    while True:
        item_id = str(input("Insert the item id: \n"))
        ITEM_MODEL["textures"]['layer0'] = MOD_ID + ':item/' + item_id
        # Serializing & save json file
        json_object = json.dumps(ITEM_MODEL, indent=4)
        with open(PATH + item_id+'.json', "w") as outfile:
            outfile.write(json_object)
            print("=======SUCCESS=======\n")


def CreateBlock():
    while True:
        block_id = str(input("Insert the block id: \n"))
        BLOCK_MODEL["textures"]['all'] = MOD_ID + ':block/' + block_id
        # Serializing & save json file
        json_object = json.dumps(BLOCK_MODEL, indent=4)
        with open(PATH + block_id+'.json', "w") as outfile:
            outfile.write(json_object)
            print("=======SUCCESS=======\n")
            # break


def CreateBlockStates():
    while True:
        block_id = str(input("Insert the block id: \n"))
        BLOCKSTATES["variants"]['']['model'] = MOD_ID + ':block/' + block_id
        # Serializing json
        json_object = json.dumps(BLOCKSTATES, indent=4)
        # Generate json file
        with open(PATH + block_id+'.json', "w") as outfile:
            outfile.write(json_object)
            print("=======SUCCESS=======\n")


def CreateBlockItem():
    while True:
        block_id = str(input("Insert the Block id\n"))
        BLOCK_ITEM["parent"] = MOD_ID + ':block/' + block_id
        # Serializing & save json file
        json_object = json.dumps(BLOCK_ITEM, indent=4)
        with open(PATH + block_id+'.json', "w") as outfile:
            outfile.write(json_object)
            print("=======SUCCESS=======\n")


# MAIN FUNC
def Main():
    print("================WELCOME================\n")
    print("Json files generator\n")
    print("1) Create Item Models")
    print("2) Create Block Models")
    print("3) Create BlockStates")
    print("4) Create Block Item Models\n")
    option = int(input('Enter your choice:'))

    if option == 1:
        CreateItem()
    elif option == 2:
        CreateBlock()
    elif option == 3:
        CreateBlockStates()
    elif option == 4:
        CreateBlockItem()
    else:
        print("Invalid option")


Main()
