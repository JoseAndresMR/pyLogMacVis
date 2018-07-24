import json
import numpy as np

class VJC(object):
    def __init__(self,vis_definition):
        self.vis_definition = vis_definition
        self.object_counter = 0
        self.json_obj = {"lws":[],"plans":{},"levels":{},"id":self.vis_definition["id"]}
        for n_page in self.vis_definition["pages"].keys():
            self.add_page(n_page)
        for level in self.vis_definition["levels"].keys():
            self.add_level(level)

        self.create_file()

    def add_page(self,n_page):
        # default_page
        page_def = self.default_page()
        for key in self.vis_definition["pages"][n_page].keys():
            if key != "structures" and key != "grid_size":
                page_def[key] = self.vis_definition["pages"][n_page][key]
            self.vis_definition["pages"][n_page]["objects"] = []

        self.json_obj["plans"][n_page] = page_def

        for n_structure in self.vis_definition["pages"][n_page]["structures"].keys():
            self.add_structure(n_page,n_structure)

    def add_structure(self,n_page,n_structure):
        struc_type = self.vis_definition["pages"][n_page]["structures"][n_structure]["type"]
        struc_area = self.get_struc_area(n_page,n_structure)

        object_list = self.default_structure(struc_type)
        
        for i in range(len(object_list)):
            object_list[i]["locx"] = object_list[i]["locx"] + struc_area["struc_pos"][0]
            object_list[i]["locy"] = object_list[i]["locy"] + struc_area["struc_pos"][1]

            self.add_object(n_page,object_list[i])
            
    def add_object(self,n_page,object_dicc):
        self.object_counter = self.object_counter + 1      
        object_dicc["object"] = self.object_counter

        self.params_to_unicode(object_dicc)
        self.json_obj["plans"][n_page]["objects"].append(object_dicc)

    def add_level(self,n_level):
        level_def = self.default_level()

        for key in self.vis_definition["levels"][n_level].keys():
            level_def[key] = self.vis_definition["levels"][n_level][key]

        self.json_obj["levels"][n_level] = level_def
        
    def create_file(self):
        path ='./data.json'
        encoded = json.dumps(self.json_obj)
        obj = open(path, 'wb')
        obj.write(encoded)
        obj.close

    def default_page(self):
        page_def = {
                "width": self.vis_definition["screen_info"]["screen_resolution"][0],
                "id": 8,
                "background": "BG_1024x1280px.jpg",
                "bgrepeat": 0,
                "bgfixed": 0,
                "locx": "",
                "bgcolor": "#E5E5E5",
                "locy": "",
                "background_add": "Bathroom_page_H.svgz",
                "sortorder": 16,
                "building": 6,
                "touch_param": "",
                "usermode_param": "",
                "pincode": "",
                "name": "Bagno",
                "layout": 0,
                "touch_bgcolor": "",
                "height": self.vis_definition["screen_info"]["screen_resolution"][1],
                "objects": []
                }
        return page_def

    def default_object(self):
        object_dicc = {
                "object": 0,
                "id": 0,
                "sortorder": 0,
                "nobg": 0,
                "locy": 0,
                "name": "",
                "type": 0,
                "locx": 0,
                "floor": 0,
                "notouch": 0
                }
        params_dicc = {
                "size":"",
                "bold":0,
                "italic":0,
                "underline":0,
                "width":0,
                "height":0,
                "displaymode":"value",
                }
        object_dicc["params"] = params_dicc

        return object_dicc

    def default_structure(self,type):
        object_list = []
        if type == 1:
            object_list.append(self.default_object())

        return object_list

    def default_level(self):
        level_def = {
                "pincode": "",
                "id": 0,
                "name": "",
                "sortorder": 0,
                "parent": 0,
                "description": ""
                }
                
        return level_def

    def params_to_unicode(self,object_dicc):
        params_dicc = object_dicc["params"]
        params_unicode = "{"
        for key in object_dicc["params"].keys():
            if params_unicode != "{":
                params_unicode = params_unicode + ","
            if type(params_dicc[key]) == str:
                params_unicode = params_unicode + "\"{0}\":\"{1}\"".format(key,object_dicc["params"][key])
            elif type(params_dicc[key]) == int:
                params_unicode = params_unicode + "\"{0}\":{1}".format(key,object_dicc["params"][key])
        params_unicode = params_unicode + "}"

        object_dicc["params"] = params_unicode

    def get_struc_area(self,n_page,n_structure):
        screen_resolution = np.asarray(self.vis_definition["screen_info"]["screen_resolution"])
        margins = np.asarray(self.vis_definition["screen_info"]["margins"])
        grid_size = np.asarray(self.vis_definition["pages"][n_page]["grid_size"])
        grid_pos = np.asarray(self.vis_definition["pages"][n_page]["structures"][n_structure]["grid_pos"])
        
        useful_resolution = screen_resolution - margins
        cell_size = useful_resolution / grid_size
        locx = margins[0] + cell_size[0] * grid_pos[0][0] \
               + cell_size[0] / 2 * ( grid_pos[0][1] - grid_pos[0][0] )
        locy = margins[1] + cell_size[1] * grid_pos[1][0] \
               + cell_size[1] / 2 * ( grid_pos[1][1] - grid_pos[1][0] )

        struc_area = {"struc_pos" : [locx,locy], "cell_size" : cell_size}

        return struc_area

    