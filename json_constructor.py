import json
import numpy as np
from Defaults_Storage import *

class VJC(object):
    def __init__(self,vis_definition):
        self.vis_definition = vis_definition
        self.dflt = Default(vis_definition)
        self.json_obj = {"lws":{},"plans":{},"levels":{},"id":self.vis_definition["id"]}

        for n_lws in self.vis_definition["lws"].keys():
            self.add_page("lws",n_lws)
        for n_page in self.vis_definition["plans"].keys():
            self.add_page("plans",n_page)
        for level in self.vis_definition["levels"].keys():
            self.add_level(level)

        self.create_file()

    def add_page(self,page_key,n_page):  # page: ["lws" or "plans"]
        if page_key == "lws":
            page_def = self.dflt.lws
        elif page_key == "plans":
            page_def = self.dflt.plans(1)

        for key in self.vis_definition[page_key][n_page].keys():
            if key != "structures" and key != "objects" and key != "grid_size":
                page_def[key] = self.vis_definition[page_key][n_page][key]

        self.json_obj[page_key][n_page] = page_def

        for n_structure in self.vis_definition[page_key][n_page]["structures"].keys():
            self.add_structure(page_key,n_page,n_structure)

        for i in range(len(self.vis_definition[page_key][n_page]["objects"])):
            self.add_object(page_key,n_page,i)

    def add_structure(self,page_key,n_page,n_structure):
        struc_area = self.get_struc_area(page_key,n_page,n_structure)

        object_list = self.dflt.structures(page_key,n_page,n_structure,struc_area)

        for i in range(len(object_list)):
            for key in self.vis_definition[page_key][n_page]["structures"][n_structure]["objects"][i].keys():
                object_list[i][key] = self.vis_definition[page_key][n_page]["structures"][n_structure]["objects"][i][key]

            object_list[i]["locx"] = object_list[i]["locx"] + struc_area["struc_pos"][0]
            object_list[i]["locy"] = object_list[i]["locy"] + struc_area["struc_pos"][1]

            self.add_object_from_struc(page_key,n_page,object_list[i])

    def add_object_from_struc(self,page_key,n_page,object_dicc):
        object_dicc["floor"] = self.vis_definition[page_key][n_page]["id"]

        if object_dicc["type"] == 0 or object_dicc["type"] == 1: 
            object_dicc["object"] = self.get_number_from_address(object_dicc["object"])

        self.params_to_unicode(object_dicc)
        self.json_obj[page_key][n_page]["objects"].append(object_dicc)

    def add_object(self,page_key,n_page,n_object):
        object_dicc = self.dflt.objects(self.vis_definition[page_key][n_page]["objects"][n_object]["type"])

        for key in self.vis_definition[page_key][n_page]["objects"][n_object].keys():
            object_dicc[key] = self.vis_definition[page_key][n_page]["objects"][n_object][key]

        if object_dicc["type"] == 0 or object_dicc["type"] == 1: 
            object_dicc["object"] = self.get_number_from_address(object_dicc["object"])

        object_dicc["floor"] = self.vis_definition[page_key][n_page]["id"]
        self.params_to_unicode(object_dicc)
        self.json_obj[page_key][n_page]["objects"].append(object_dicc)

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

    def params_to_unicode(self,object_dicc):   # Abreviar esta funcion
        object_dicc["params"] = self.dicc_to_unicode(object_dicc["params"])

    def dicc_to_unicode(self,dicc_to_change):
        dicc_in_unicode = ""
        for key in dicc_to_change.keys():
            if dicc_in_unicode != "":
                dicc_in_unicode = dicc_in_unicode + ","
            if type(dicc_to_change[key]) == int:
                dicc_in_unicode = dicc_in_unicode + "\"{0}\":{1}".format(key,dicc_to_change[key])
            elif dicc_to_change[key] == "null":
                dicc_in_unicode = dicc_in_unicode + "\"{0}\":null".format(key)
            elif dicc_to_change[key] == "false":
                dicc_in_unicode = dicc_in_unicode + "\"{0}\":false".format(key)
            elif type(dicc_to_change[key]) == list:
                sub_list_in_unicode = ""
                for i in range(len(dicc_to_change[key])):
                    if sub_list_in_unicode != "":
                        sub_list_in_unicode = sub_list_in_unicode + ","
                    sub_dicc_in_unicode = self.dicc_to_unicode(dicc_to_change[key][i])
                    sub_list_in_unicode = sub_list_in_unicode + sub_dicc_in_unicode
                sub_list_in_unicode = "[" + sub_list_in_unicode + "]"
                dicc_in_unicode = dicc_in_unicode + '\"{0}\":{1}'.format(key,sub_list_in_unicode)

            elif type(dicc_to_change[key]) == str:
                dicc_in_unicode = dicc_in_unicode + "\"{0}\":\"{1}\"".format(key,dicc_to_change[key])

        dicc_in_unicode = "{" + dicc_in_unicode + "}"

        return dicc_in_unicode

    def get_struc_area(self,page_key,n_page,n_structure):
        screen_resolution = np.asarray(self.vis_definition["screen_info"]["screen_resolution"])
        margins = np.asarray(self.vis_definition["screen_info"]["margins"])
        grid_size = np.asarray(self.vis_definition["plans"][n_page]["grid_size"])
        grid_pos = np.asarray(self.vis_definition["plans"][n_page]["structures"][n_structure]["grid_pos"])
        
        useful_resolution = screen_resolution - margins*2
        cell_size = useful_resolution / grid_size
        locx = margins[0] + cell_size[0] * (grid_pos[0][0]-1)
        locy = margins[1] + cell_size[1] * (grid_pos[1][0]-1)

        struc_area = {"struc_pos" : [locx,locy], "cell_size" : cell_size}

        return struc_area

    def get_number_from_address(self,address):
        splitted = np.asarray(str.split(address,"/"))
        number = int(splitted[2]) +\
                 int(splitted[1]) * 256 +\
                 int(splitted[0]) * 8 * 256
        print number

        return number