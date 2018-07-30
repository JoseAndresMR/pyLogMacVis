from json_constructor import VJC
import os
import csv

vis_definition= {
    "pages": {
        "1":{
            "name": "level 2 A",
            "building": 3,
            "id": 1,
            "background": "BG_1024x1280px.jpg",
            "layout": 6,
            "structures":{
                "1": {
                    "type" : 1,
                    "grid_pos" : [[1,1],[1,1]],
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
                    "name" : "nivel 2 B",
                    "type" : 2
                }
            
            ],
            "grid_size" : [1,1]
        },
        "2":{
            "name": "level 2 B",
            "building": 4,
            "id": 2,
            "background": "BG_1024x1280px.jpg",
            "layout" : 6,
            "structures":{
                "1": {
                    "type" : 1,
                    "grid_pos" : [[1,2],[1,1]],
                    "objects" : [
                        {
                            "id" : 1
                        },
                        {
                            "id" : 2
                        }
                    ]
                },
            },
            "objects": [
                {
                    "name" : "nivel 2 A",
                    "type" : 2
                }
            ],
            "grid_size" : [2,2]
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
            "name" : "nivel 2 A",
            "sortorder": 2,
            "parent": 2
        },
        "4": {
            "id" : 4,
            "name" : "nivel 2 B",
            "sortorder": 2,
            "parent": 2
        }
    },
    "id" : 2, # Debe apuntar siempre a uno de los niveles definidos
    "screen_info" : {
        "screen_resolution" : [500,500],
        "margins" : [10,10]
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