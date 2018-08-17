from json_constructor import VJC
import os
import csv
import numpy as np
import pandas as pd
import ast
from itertools import izip

vis_definition= {
    "lws":{},
    "plans": {},
    "levels": {"2": {"id" : 2,"name" : "nivel 1","sortorder": 1,"parent": 0}}
}

a = izip(*csv.reader(open("data_frame_prueba.csv", "rb")))
csv.writer(open("data_frame_prueba_translated.csv", "wb")).writerows(a)
df = pd.read_csv('data_frame_prueba_translated.csv')

for key_1 in df.keys():
    key_1_splitted = key_1.split()

    #### Global ####
    if key_1 == "Global":
        vis_definition["id"] = str(df[key_1][0])
        vis_definition["screen_info"]={}
        vis_definition["screen_info"]["screen_resolution"] = ast.literal_eval(df[key_1][1])
        vis_definition["screen_info"]["margins"] = ast.literal_eval(df[key_1][2])

    #### Paginas ####
    elif key_1_splitted[0][0] == "P":
        plan = key_1_splitted[0][1:]

        if plan not in vis_definition["plans"].keys():
            vis_definition["plans"][plan] = {"structures" : {}, "objects" : []}

        #### Definicion pagina ####
        if len(key_1_splitted) == 1:
            vis_def_plan = vis_definition["plans"][plan]
            vis_def_plan["id"] = int(plan)
            vis_def_plan["name"] = df[key_1][0]
            vis_def_plan["grid_size"] = ast.literal_eval(df[key_1][1])
            vis_def_plan["building"] = int(plan) + 3

            #### Definicion nivel simple ####
            vis_definition["levels"][str(int(plan)+3)] = {}
            vis_definition["levels"][str(int(plan)+3)]["id"] = int(plan)+3
            vis_definition["levels"][str(int(plan)+3)]["name"] = df[key_1][0]
            vis_definition["levels"][str(int(plan)+3)]["sortorder"] = 2
            vis_definition["levels"][str(int(plan)+3)]["parent"] = 2

        else:
            if (key_1_splitted[1][0]) == "E":
                structure = key_1_splitted[1][1:]

                if structure not in vis_definition["plans"][plan]["structures"].keys():
                    vis_definition["plans"][plan]["structures"][structure] = {"objects" : []}

                #### Tipos de estructuras ####
                vis_def_structure = vis_definition["plans"][plan]["structures"][structure]
                struc_type = int(df[key_1][0])
                if struc_type == 1:
                    vis_def_structure["type"] = int(df[key_1][0])
                    vis_def_structure["grid_pos"] = ast.literal_eval(df[key_1][1])
                    vis_def_structure["objects"].append({"object" : df[key_1][2]})
                    vis_def_structure["objects"].append({"name" : df[key_1][3]})

                if struc_type == 2:
                    vis_def_structure["type"] = int(df[key_1][0])
                    vis_def_structure["grid_pos"] = ast.literal_eval(df[key_1][1])
                    vis_def_structure["objects"].append({"object" : df[key_1][2]})
                    vis_def_structure["objects"].append({"name" : df[key_1][3]})
                    vis_def_structure["objects"].append({"object" : df[key_1][4]})
                    vis_def_structure["objects"].append({})
                    
                if struc_type == 3:
                    vis_def_structure["type"] = int(df[key_1][0])
                    vis_def_structure["grid_pos"] = ast.literal_eval(df[key_1][1])
                    vis_def_structure["objects"].append({"object" : df[key_1][2]})
                    vis_def_structure["objects"].append({"object" : df[key_1][3]})
                    vis_def_structure["objects"].append({"object" : df[key_1][4]})
                    vis_def_structure["objects"].append({})

VJC(vis_definition)

os.system("tar -cvf archivo.tar data.json > /dev/null")
os.system("zip -r icons.zip icons > /dev/null")
os.system("zip -r img.zip img > /dev/null")