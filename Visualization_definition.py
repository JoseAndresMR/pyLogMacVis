from json_constructor import VJC
import os

vis_definition= {
    "pages": {
        "1":{
            "structures":{
                "1": {
                    "type" : 1,
                    "grid_pos" : [[1,2],[1,2]]
                }
            },
            "grid_size" : [3,4]
        },
        "2": {
            "structures":{
                "1": {
                    "type" : 1,
                    "grid_pos" : [[2,2],[1,2]]
                }
            },
            "grid_size" : [3,4]
        }
    },
    "levels": {
        "1": {
            "id" : 1,
            "name" : "nivel"
        }
    },
    "id" : 1,
    "screen_info" : {
        "screen_resolution" : [1024,748],
        "margins" : [50,50]
    }   
}


VJC(vis_definition)

os.system("tar -cvf archivo.tar data.json icons.tar.gz img.tar.gz")