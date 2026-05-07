from omni.isaac.core.utils.prims import create_prim

def setup_all_lights():
    create_prim(
        prim_path = "/World/MainLight",
        prim_type = "DistantLight",
        attributes = {
            "inputs:intensity" : 500.0, 
            "inputs:color": (1.0, 1.0, 1.0)
            }
    )

    # create_prim(
    #     prim_path = "/World/PointLight",
    #     prim_type = "SphereLight",
    #     attributes = {
    #         "inputs:intensity" : 5000.0, 
    #         "inputs:color" : (0.2, 0.2, 1.0),
    #         "inputs:radius" : 1.0
    #         }
    # )
