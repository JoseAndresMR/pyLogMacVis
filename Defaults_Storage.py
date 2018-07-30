import numpy as np

class Default(object):
    def __init__(self,vis_definition):
        self.vis_definition = vis_definition

    def objects(self,type):
        if type == 0:
            object_dicc = {
                "object": 0,
                "id": 0,
                "params": {"size":"","color":"","font":"","bold":0,"italic":0,"underline":0,"width":30,"height":30,"icon_on":"vidgets-dot_on.svg","icon_off":"vidgets-dot_off.svg","icons_add":[],"displaymode":"icon","showcontrol":0,"fixedvalue":"","update":"false","pincode":"","widget":"null","backdrop":0},
                "sortorder": 1,
                "nobg": 1,
                "statusobject": 0,
                "readonly": 0,
                "name": "",
                "locy": 0,
                "type": 0,
                "locx": 0,
                "floor": 0,
                "notouch": 0,
                "visparams" : "",
            }

        elif type == 1:
            object_dicc = {
                "object": 0,
                "id": 0,
                "params": {"size":"","color":"","font":"","bold":0,"italic":0,"underline":0,"width":140,"height":130,"icon_default":"S_01_02_scene-03.svg","icons_add":[{"min":1,"max":1,"icon":"S_01_02_scene-04.svg"},{"min":2,"max":2,"icon":"S_01_02_scene-03.svg"},{"min":3,"max":3,"icon":"S_01_02_scene-04.svg"}],"displaymode":"icon","showcontrol":0,"fixedvalue":"2","update":"false","pincode":"","widget":"null","backdrop":0},
                "sortorder": 1,
                "cls": "",
                "nobg": 1,
                "statusobject": 0,
                "readonly": 0,
                "name": "",
                "locy": 0,
                "type": 1,
                "locx": 0,
                "floor": 0,
                "notouch": 0
            }

        elif type == 2:    # Boton para ir a otras paginas. El "id" de esa pagina debe ser...
            object_dicc = {
                "object": 0,    # ... este
                "id": 0,
                "params": {"size":"","bold":0,"italic":0,"underline":0,"width":440,"height":84,"displaymode":"icon","icon":"socket.svg","icon_active":"socket.svg"},
                "sortorder": 4,
                "cls": "",
                "nobg": 1,
                "locy": 0,
                "name": "",
                "type": 2,
                "locx": 0,
                "floor": 0,
                "notouch": 0
            }
        
        elif type == 3:
            object_dicc = {
            }
  
        elif type == 4:
            object_dicc = {
                "object": 0,
                "id": 0,
                "params": {"autoopen":1,"width":"32","win_width":"480","height":"32","win_height":"360","src":"http://188.134.79.111:8080/anony/mjpg.cgi","icon":"camera.png"},
                "cls": "",
                "nobg": 1,
                "floor": 0,
                "locy": 0,
                "type": 4,
                "locx": 0,
                "name": ""
            }

        elif type == 5:
            object_dicc = {
            }

        elif type == 6:
            object_dicc = {
                "locy": 0,
                "id": 0,
                "params": {"size":28,"color":"#FFFFFF","font":"Verdana","bold":0,"italic":0,"underline":0},
                "floor": 0,
                "type": 6,
                "nobg": 1,
                "name": "",
                "locx": 0
            }

        elif type == 7:
            object_dicc = {
                "locy": 0,
                "locx": 0,
                "id": 0,
                "params": {"source":"local","src":"vidgets-18.svg","width":"","height":"","link":""},
                "nobg": 1,
                "floor": 0,
                "type": 7
            }

        elif type == 8:
            object_dicc = {
            }

        elif type == 9:
            object_dicc = {
                "locy": 0,
                "id": 0,
                "params": {"source":"url","url":"http://89.179.246.19:3012/cgi-bin/audio/launcher.cgi","width":"270","height":"400"},
                "cls": "",
                "nobg": 1,
                "name": "",
                "type": 9,
                "locx": 0,
                "floor": 0,
                "notouch": 0
            }
        
        return object_dicc

    def lws(self,type):
        page_def = {
            "width": self.vis_definition["screen_info"]["screen_resolution"][0],
            "layout": 0,
            "id": 1,
            "background": "empty.png",
            "adminonly": 0,
            "building": 0,
            "name": "all",
            "usermode_param": "",
            "bgcolor": "#FFFFFF",
            "sortorder": 1,
            "bgrepeat": 0,
            "type": "layout",
            "touch_param": "",
            "height": self.vis_definition["screen_info"]["screen_resolution"][1],
            "objects": []
        }

        return page_def

    def pages(self,type):
        if type == 1:
            page_def = {
                "width": self.vis_definition["screen_info"]["screen_resolution"][0],
                "id": 1,
                "background": "",
                "bgrepeat": 0,
                "bgfixed": 0,
                "locx": "",
                "bgcolor": "#E5E5E5",
                "locy": "",
                # "background_add": "",
                "sortorder": 16,
                "building": 6,
                "touch_param": "",
                "usermode_param": "",
                "pincode": "",
                "name": "Bagno",
                "layout": 1,
                "touch_bgcolor": "",
                "height": self.vis_definition["screen_info"]["screen_resolution"][1],
                "objects": []
            }

        return page_def

    def structures(self,n_page,n_structure,struc_area):
        object_list = []
        object_dicc_newinfo_list = []
        struc_type = self.vis_definition["pages"][n_page]["structures"][n_structure]["type"]
        grid_pos = np.asarray(self.vis_definition["pages"][n_page]["structures"][n_structure]["grid_pos"])
        cell_size = [struc_area["cell_size"][0]*(grid_pos[0][1]-grid_pos[0][0]+1),\
                     struc_area["cell_size"][1]*(grid_pos[1][1]-grid_pos[1][0]+1)]

        # Todos los datos geometricos de longitud estan en porcentage de cell_size
        if struc_type == 1:
            # Objeto 1
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 20,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    "width" : int(cell_size[0]/100 * 10),
                    "height" : int(cell_size[1]/100 * 10)
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

            # Objeto 2
            object_dicc_newinfo = {
                "type": 6,
                "locx" : cell_size[0]/100.0 * 70,
                "locy" : cell_size[1]/100.0 * 50,
                "name" : "prueba",
                "params" : {
                    "size" : int(cell_size[1]/100.0 * 10)
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

        if struc_type == 2:
            object_list.append(self.objects(0))
            object_list.append(self.objects(6))


        
        for i in range(len(object_dicc_newinfo_list)):
            object_list.append(self.objects(object_dicc_newinfo_list[i]["type"]))
            for key in object_dicc_newinfo_list[i].keys():
                if key == "params":
                    for param_key in object_dicc_newinfo_list[i][key].keys(): 
                        if param_key == "icons_add":
                            for j in range(len(object_dicc_newinfo_list[i][key][param_key])):
                                for icons_key in object_dicc_newinfo_list[i][key][param_key][j].keys():
                                    object_list[i][key][param_key][j][icons_key] = object_dicc_newinfo_list[i][key][param_key][j][icons_key]
                        else:
                            object_list[i][key][param_key] = object_dicc_newinfo_list[i][key][param_key]
                else:
                    object_list[i][key] = object_dicc_newinfo_list[i][key]

        for i in range(len(object_list)):
            if "width" in object_list[i]["params"].keys():
                object_list[i]["locx"] = object_list[i]["locx"] - object_list[i]["params"]["width"]/2.0
                object_list[i]["locy"] = object_list[i]["locy"] - object_list[i]["params"]["height"]/2.0
            elif "size" in object_list[i]["params"].keys():
                object_list[i]["locx"] = object_list[i]["locx"] - object_list[i]["params"]["size"]*len(object_list[i]["name"])*0.9/2.0
                object_list[i]["locy"] = object_list[i]["locy"] - object_list[i]["params"]["size"]*1.1/2.0

        return object_list

    def levels(self):
        level_def = {
            "pincode": "",
            "id": 0,
            "name": "",
            "sortorder": 0,
            "parent": 0,
            "description": ""
        }
                
        return level_def