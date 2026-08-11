from engine.screen import Screen
from engine.projection import Projector
from engine.lighting import Light3D
from engine.obj_loader import Model_Converter
import time

screen = Screen(100, 40)
projector = Projector()
light = Light3D()
converter = Model_Converter()

mesh = converter.convert_obj_file("files/example_models/cube.obj")

mesh.calculate_center()

screen.render()

mesh.rotate(30,0,0)

while(True):
    lit_mesh = light.directional_light_prediction(mesh, direction=[-1,-1,-2])
    proj_mesh = projector.perspective_proj(mesh=lit_mesh, width=100, height=40, scale=10, aspect_ratio=2, depth_scale=0.2, default_depth=-5)
    screen.draw_faces(proj_mesh)
    screen.render(show_errors=False)
    mesh.rotate(0,-2,0)
    time.sleep(0.03)
    screen.clear()
