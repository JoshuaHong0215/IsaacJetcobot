from omni.isaac.core.utils.prims import create_prim

def setup_all_lights():
    create_prim(
        prim_path = "/World/MainLight",
        prim_type = "DistantLight",
        attributes = {"intensity" : 1000, "color": (1.0, 1.0, 1.0)}
    )

    create_prim(
        prim_path = "/World/PointLight",
        prim_type = "SphereLight",
        attributes = {"intensity" : 5000, "color" : (0.2, 0.2, 1.0)}
    )
