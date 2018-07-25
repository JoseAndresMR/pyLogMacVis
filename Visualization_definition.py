from json_constructor import VJC
import os
import csv

vis_definition= {
    "pages": {
        "1":{
            "name": "nivel 1",
            "building": 2,
            "background": "BG_1024x1280px.jpg",
            "structures":{
                "1": {
                    "type" : 2,
                    "grid_pos" : [[1,2],[1,2]],
                    "objects" : [
                        {
                            "id" : 1
                        },
                        {
                            "id" : 2
                        }
                    ]
                }
            },
            "objects": [
                {
                    "object": 9,
                    "id": 3,
                    "sortorder": 4,
                    "cls": "",
                    "nobg": 1,
                    "statusobject": 9,
                    "readonly": 0,
                    "name": "",
                    "locy": 50,
                    "type": 0,
                    "locx": 50,
                    "floor": 1,
                    "notouch": 0,
                    "params": {"size":"","color":"","font":"","bold":0,"italic":0,"underline":0,"width":139,"height":129,"icon_on":"bulb-active.svg","icon_off":"bulb.svg","icons_add":"[]","displaymode":"icon","showcontrol":0,"fixedvalue":"","update":"false","pincode":"","widget":"null","backdrop":0}
                },
                {
                    "object": 9,
                    "id": 4,
                    "sortorder": 4,
                    "cls": "",
                    "nobg": 1,
                    "statusobject": 9,
                    "readonly": 0,
                    "name": "",
                    "locy": 100,
                    "type": 0,
                    "locx": 100,
                    "floor": 1,
                    "notouch": 0,
                    "params": {"size":"","color":"","font":"","bold":0,"italic":0,"underline":0,"width":139,"height":129,"icon_on":"bulb-active.svg","icon_off":"bulb.svg","icons_add":"[]","displaymode":"icon","showcontrol":0,"fixedvalue":"","update":"false","pincode":"","widget":"null","backdrop":0}
                }
            ],
            "grid_size" : [3,4]
        }
    },
    "levels": {
        "2": {
            "id" : 2, # Pasa a ser "building" en sus paginas
            "name" : "nivel 1",
            "sortorder": 1,
            "parent": 0
        },
        "3": {
            "id" : 3,
            "name" : "nivel 2",
            "sortorder": 1,
            "parent": 2
        }
    },
    "id" : 2, # Debe apuntar siempre a uno de los niveles definidos
    "screen_info" : {
        "screen_resolution" : [644,361],
        "margins" : [50,50]
    }   
}

# f = open('data.csv','wb')
# w = csv.DictWriter(f,vis_definition.keys())
# w.writerows(vis_definition)
# f.close()

# w = csv.DictWriter( sys.stdout, vis_definition.keys() )
# for key,val in sorted(vis_definition.items()):
#     row = {'org': key}
#     row.update(val)
#     w.writerow(row)

VJC(vis_definition)

os.system("tar -cvf icons.tar.gz icons > /dev/null")
os.system("tar -cvf img.tar.gz img > /dev/null")
os.system("tar -cvf archivo.tar data.json icons.tar.gz img.tar.gz > /dev/null")