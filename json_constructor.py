import json
import numpy as np
from Defaults_Storage import *

class VJC(object):
    def __init__(self,vis_definition):
        self.vis_definition = vis_definition
        self.dflt = Default(vis_definition)
        self.json_obj = {"lws":[],"plans":{},"levels":{},"id":self.vis_definition["id"]}
        for n_page in self.vis_definition["pages"].keys():
            self.add_page(n_page)
        for level in self.vis_definition["levels"].keys():
            self.add_level(level)

        self.create_file()

    def add_page(self,n_page):
        # default_page
        page_def = self.dflt.pages(1)
        for key in self.vis_definition["pages"][n_page].keys():
            if key != "structures" and key != "objects" and key != "grid_size":
                page_def[key] = self.vis_definition["pages"][n_page][key]

        self.json_obj["plans"][n_page] = page_def

        for n_structure in self.vis_definition["pages"][n_page]["structures"].keys():
            self.add_structure(n_page,n_structure)

        for i in range(len(self.vis_definition["pages"][n_page]["objects"])):
            self.add_object(n_page,i)

    def add_structure(self,n_page,n_structure):
        struc_area = self.get_struc_area(n_page,n_structure)

        object_list = self.dflt.structures(n_page,n_structure,struc_area)

        for i in range(len(object_list)):
            for key in self.vis_definition["pages"][n_page]["structures"][n_structure]["objects"][i].keys():
                object_list[i][key] = self.vis_definition["pages"][n_page]["structures"][n_structure]["objects"][i][key]

            object_list[i]["locx"] = object_list[i]["locx"] + struc_area["struc_pos"][0]
            object_list[i]["locy"] = object_list[i]["locy"] + struc_area["struc_pos"][1]

            print object_list[i]["locx"]
            print object_list[i]["locy"]

            self.add_object_from_struc(n_page,object_list[i])

    def add_object_from_struc(self,n_page,object_dicc):
        self.params_to_unicode(object_dicc)
        self.json_obj["plans"][n_page]["objects"].append(object_dicc)

    def add_object(self,n_page,n_object):
        object_dicc = self.dflt.objects(self.vis_definition["pages"][n_page]["objects"][n_object]["type"])

        for key in self.vis_definition["pages"][n_page]["objects"][n_object].keys():
            object_dicc[key] = self.vis_definition["pages"][n_page]["objects"][n_object][key]

        self.params_to_unicode(object_dicc)
        self.json_obj["plans"][n_page]["objects"].append(object_dicc)

    def add_level(self,n_level):
        level_def = self.dflt.levels()

        for key in self.vis_definition["levels"][n_level].keys():
            level_def[key] = self.vis_definition["levels"][n_level][key]

        self.json_obj["levels"][n_level] = level_def
        
    def create_file(self):
        path ='./data.json'
        encoded = json.dumps(self.json_obj)
        obj = open(path, 'wb')
        obj.write(encoded)
        obj.close

    def params_to_unicode(self,object_dicc):
        params_dicc = object_dicc["params"]
        params_unicode = "{"
        for key in object_dicc["params"].keys():
            if params_unicode != "{":
                params_unicode = params_unicode + ","
            if type(params_dicc[key]) == int:
                params_unicode = params_unicode + "\"{0}\":{1}".format(key,object_dicc["params"][key])
            elif type(params_dicc[key]) == str and params_dicc[key] == "null":
                params_unicode = params_unicode + "\"{0}\":null".format(key)
            elif type(params_dicc[key]) == str and params_dicc[key] == "false":
                params_unicode = params_unicode + "\"{0}\":false".format(key)
            elif type(params_dicc[key]) == str and params_dicc[key] == "[]":
                params_unicode = params_unicode + "\"{0}\":[]".format(key)
            elif type(params_dicc[key]) == str:
                params_unicode = params_unicode + "\"{0}\":\"{1}\"".format(key,object_dicc["params"][key])

        params_unicode = params_unicode + "}"

        object_dicc["params"] = params_unicode

    def get_struc_area(self,n_page,n_structure):
        screen_resolution = np.asarray(self.vis_definition["screen_info"]["screen_resolution"])
        margins = np.asarray(self.vis_definition["screen_info"]["margins"])
        grid_size = np.asarray(self.vis_definition["pages"][n_page]["grid_size"])
        grid_pos = np.asarray(self.vis_definition["pages"][n_page]["structures"][n_structure]["grid_pos"])
        
        useful_resolution = screen_resolution - margins*2
        cell_size = useful_resolution / grid_size
        locx = margins[0] + cell_size[0] * (grid_pos[0][0]-1)
        locy = margins[1] + cell_size[1] * (grid_pos[1][0]-1)

        struc_area = {"struc_pos" : [locx,locy], "cell_size" : cell_size}


        return struc_area