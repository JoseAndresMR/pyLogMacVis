import numpy as np

class Default(object):
    def __init__(self,vis_definition):
        self.vis_definition = vis_definition

    def objects(self,type):
        if type == 0:
            object_dicc = {
                "object": "1/1/5",
                "id": 0,
                "params": {"size":"","color":"","font":"","bold":0,"italic":0,"underline":0,"width":30,"height":30,"icon_on":"","icon_off":"","icons_add":[],"displaymode":"icon","showcontrol":0,"fixedvalue":"","update":"false","pincode":"","widget":"null","backdrop":0},
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
                "object": "1/1/5",
                "id": 0,
                "params": {"size":"","color":"","font":"","bold":0,"italic":0,"underline":0,"width":140,"height":130,"icon_default":"","icons_add":[],"displaymode":"icon","showcontrol":0,"fixedvalue":"","update":"false","pincode":"","widget":"null","backdrop":0},
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
                "object": "1/1/5",
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

    def lws(self):
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

    def plans(self,type):
        if type == 1:
            page_def = {
                "width": self.vis_definition["screen_info"]["screen_resolution"][0],
                "id": 1,
                "background": "TOLEDO.jpg",
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
                "layout": 6,
                "touch_bgcolor": "",
                "height": self.vis_definition["screen_info"]["screen_resolution"][1],
                "objects": []
            }

        return page_def

    def structures(self,page_key,n_page,n_structure,struc_area):
        object_list = []
        object_dicc_newinfo_list = []
        struc_type = self.vis_definition[page_key][n_page]["structures"][n_structure]["type"]
        grid_pos = np.asarray(self.vis_definition[page_key][n_page]["structures"][n_structure]["grid_pos"])
        cell_size = [struc_area["cell_size"][0]*(grid_pos[0][1]-grid_pos[0][0]+1),\
                     struc_area["cell_size"][1]*(grid_pos[1][1]-grid_pos[1][0]+1)]

        # Todos los datos geometricos de longitud estan en porcentage de cell_size
        if struc_type == "title":
            # Objeto 1
            object_dicc_newinfo = {
                "type": 6,
                "locx" : cell_size[0]/100.0 * 50,
                "locy" : cell_size[1]/100.0 * 50,
                "name" : "titulo",
                "params" : {
                    "size" : int(min(cell_size[0], cell_size[1])/100.0 * 65),
                    "translation": "string"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

        if struc_type == 1:
            # Objeto 1
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 20,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    "width" : int(min(cell_size[0], cell_size[1])/100.0 * 70),
                    "height" : int(min(cell_size[0], cell_size[1])/100.0 * 70),
                    "icon_on": "party-active.svg",
                    "icon_off": "party.svg",
                    "translation": "dimensions"
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
                    "size" : int(min(cell_size[0], cell_size[1])/100.0 * 40),
                    "translation": "string"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

        if struc_type == 2:
            # Objeto 1
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 40,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    "width" : int(min(cell_size[0], cell_size[1])/100.0 * 60),
                    "height" : int(min(cell_size[0], cell_size[1])/100.0 * 60),
                    "icon_on": "party-active.svg",
                    "icon_off": "party.svg",
                    "translation": "dimensions"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

            # Objeto 2
            object_dicc_newinfo = {
                "type": 6,
                "locx" : cell_size[0]/100.0 * 80,
                "locy" : cell_size[1]/100.0 * 50,
                "name" : "prueba",
                "params" : {
                    "size" : int(min(cell_size[0], cell_size[1])/100.0 * 30),
                    "translation": "string"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

            # Objeto 3
            object_dicc_newinfo = {
                "type": 1,
                "locx" : cell_size[0]/100.0 * 15,
                "locy" : cell_size[1]/100.0 * 50,
                "name" : "",
                "readonly": 1,
                "params" : {
                    "size" : int(min(cell_size[0], cell_size[1])/100.0 * 30),
                    "translation": "size",
                    "displaymode": "value"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

        if struc_type == 3:
            # Objeto 1
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 25,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    "width" : int(min(cell_size[0], cell_size[1])/100.0 * 60),
                    "height" : int(min(cell_size[0], cell_size[1])/100.0 * 60),
                    "icon_on": "minus.svg",
                    "icon_off": "minus.svg",
                    "fixedvalue": 0,
                    "displaymode": "icon",
                    "translation": "dimensions"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

            # Objeto 2
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 50,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    # "width" : int(min(cell_size[0], cell_size[1])/100.0 * 30),
                    # "height" : int(min(cell_size[0], cell_size[1])/100.0 * 30),
                    "size": int(min(cell_size[0], cell_size[1])/100.0 * 30),
                    "displaymode": "value",
                    "translation": "size"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

            # Objeto 3
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 75,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    "width" : int(min(cell_size[0], cell_size[1])/100.0 * 60),
                    "height" : int(min(cell_size[0], cell_size[1])/100.0 * 60),
                    "icon_on": "plus.svg",
                    "icon_off": "plus.svg",
                    "fixedvalue": 1,
                    "displaymode": "icon",
                    "translation": "dimensions"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

            # Objeto 4
            object_dicc_newinfo = {
                "type": 7,
                "locx" : cell_size[0]/100.0 * 50,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    "width" : int(cell_size[0]/100.0 * 100),
                    "height" : int(cell_size[1]/100.0 * 100),
                    "src": "13EE3E61.jpg",
                    "translation": "dimensions"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

        if struc_type == 4:
            # Objeto 1
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 25,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    "width" : int(min(cell_size[0], cell_size[1])/100.0 * 60),
                    "height" : int(min(cell_size[0], cell_size[1])/100.0 * 60),
                    "icon_on": "minus.svg",
                    "icon_off": "minus.svg",
                    "fixedvalue": 0,
                    "displaymode": "icon",
                    "translation": "dimensions"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

            # Objeto 2
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 50,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    # "width" : int(min(cell_size[0], cell_size[1])/100.0 * 30),
                    # "height" : int(min(cell_size[0], cell_size[1])/100.0 * 30),
                    "size": int(min(cell_size[0], cell_size[1])/100.0 * 30),
                    "displaymode": "value",
                    "translation": "size"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)

        if struc_type == 5:
            # Objeto 1
            object_dicc_newinfo = {
                "type": 0,
                "locx" : cell_size[0]/100.0 * 20,
                "locy" : cell_size[1]/100.0 * 50,
                "params" : {
                    "width" : int(min(cell_size[0], cell_size[1])/100.0 * 70),
                    "height" : int(min(cell_size[0], cell_size[1])/100.0 * 70),
                    "icon_on": "party-active.svg",
                    "icon_off": "party.svg",
                    "translation": "dimensions"
                }
            }
            object_dicc_newinfo_list.append(object_dicc_newinfo)
        
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
            if object_list[i]["params"]["translation"] == "dimensions":
                object_list[i]["locx"] = object_list[i]["locx"] - object_list[i]["params"]["width"]/2.0
                object_list[i]["locy"] = object_list[i]["locy"] - object_list[i]["params"]["height"]/2.0
            
            elif object_list[i]["params"]["translation"] == "string":
                object_list[i]["locx"] = object_list[i]["locx"] - object_list[i]["params"]["size"]*len(object_list[i]["name"])*0.9/2.0
                object_list[i]["locy"] = object_list[i]["locy"] - object_list[i]["params"]["size"]*1.1/2.0

            elif object_list[i]["params"]["translation"] == "size":
                object_list[i]["locx"] = object_list[i]["locx"] - object_list[i]["params"]["size"]*3/2.0
                object_list[i]["locy"] = object_list[i]["locy"] - object_list[i]["params"]["size"]*1.1/2.0

            del(object_list[i]["params"]["translation"])

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