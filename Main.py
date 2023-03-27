# @Author : Charly1307
# Version : 1.1

import os
import json

# IMPORTANT, CHANGE PATH AND MOD_ID!
PATH = os.path.join("C:/Users/carlos/Desktop/JsonFiles/")
MOD_ID = "decorock"

# DON'T CHANGE THE FORMAT!
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
        json_object = json.dumps(ITEM_MODEL, indent=4)
        with open(PATH + item_id+'.json', "w") as outfile:
            outfile.write(json_object)
            print("=======SUCCESS=======\n")


def CreateBlock():
    while True:
        block_id = str(input("Insert the block id: \n"))
        BLOCK_MODEL["textures"]['all'] = MOD_ID + ':block/' + block_id
        json_object = json.dumps(BLOCK_MODEL, indent=4)
        with open(PATH + block_id+'.json', "w") as outfile:
            outfile.write(json_object)
            print("=======SUCCESS=======\n")


def CreateBlockStates():
    while True:
        block_id = str(input("Insert the block id: \n"))
        BLOCKSTATES["variants"]['']['model'] = MOD_ID + ':block/' + block_id
        json_object = json.dumps(BLOCKSTATES, indent=4)
        with open(PATH + block_id+'.json', "w") as outfile:
            outfile.write(json_object)
            print("=======SUCCESS=======\n")


def CreateBlockItem():
    while True:
        block_id = str(input("Insert the Block id\n"))
        BLOCK_ITEM["parent"] = MOD_ID + ':block/' + block_id
        json_object = json.dumps(BLOCK_ITEM, indent=4)
        with open(PATH + block_id+'.json', "w") as outfile:
            outfile.write(json_object)
            print("=======SUCCESS=======\n")


def Main():
    try:
        print("================WELCOME================\n")
        print("Json files generator\n")
        print("1) Create Item Models")
        print("2) Create Block Models")
        print("3) Create BlockStates")
        print("4) Create Block Item Models")
        print("5) Exit\n")
        option = int(input('Enter your choice:'))
        try:
            if option == 1:
                CreateItem()
            elif option == 2:
                CreateBlock()
            elif option == 3:
                CreateBlockStates()
            elif option == 4:
                CreateBlockItem()
            elif option == 5:
                exit()
            else:
                print("Invalid option")
        except KeyboardInterrupt:
            print("\n================BACK================\n")
            Main()
    except KeyboardInterrupt:
        print("\n================EXIT================\n")
        exit()


Main()
