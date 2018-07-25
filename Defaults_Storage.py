class Default(object):
    def __init__(self,vis_definition):
        self.vis_definition = vis_definition

    def objects(self,type):
        if type == 0:
            object_dicc = {
                "object": 0,
                "id": 0,
                "params": {"size":"","color":"","font":"","bold":0,"italic":0,"underline":0,"width":16,"height":16,"icon_on":"vidgets-dot_on.svg","icon_off":"vidgets-dot_off.svg","icons_add":"[]","displaymode":"icon","showcontrol":0,"fixedvalue":"","update":"false","pincode":"","widget":"null","backdrop":0},
                "sortorder": 1,
                "nobg": 1,
                "statusobject": 0,
                "readonly": 1,
                "name": "",
                "locy": 0,
                "type": 0,
                "locx": 0,
                "floor": 0,
                "notouch": 0
            }

        elif type == 1:
            object_dicc = {
                "object": 0,
                "id": 0,
                "params": {"size":"","color":"","font":"","bold":0,"italic":0,"underline":0,"width":140,"height":130,"icon_default":"S_01_02_scene-03.svg","icons_add":[{"min":1,"max":1,"icon":"S_01_02_scene-04.svg"},{"min":2,"max":2,"icon":"S_01_02_scene-03.svg"},{"min":3,"max":3,"icon":"S_01_02_scene-04.svg"}],"displaymode":"icon","showcontrol":0,"fixedvalue":"2","update":false,"pincode":"","widget":null,"backdrop":0},
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

        elif type == 2:
            object_dicc = {
                "object": 0,
                "id": 0,
                "params": {"size":"","bold":0,"italic":0,"underline":0,"width":440,"height":84,"displaymode":"icon","icon":"S_01_02_plan_link-01.svg","icon_active":"S_01_02_plan_link-02.svg"},
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

    def structures(self,type):
        object_list = []
        if type == 1:
            object_list.append(self.objects(0))
            object_list.append(self.objects(0))

        if type == 2:
            object_list.append(self.objects(0))
            object_list.append(self.objects(6))

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