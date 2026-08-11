from .math3d import Vector3
from .mesh import Mesh

class Projector():
    def ortographic_proj(self, mesh, width, height, scale=2, aspect_ratio=1.8):
        proj_mesh = []
       
        cx = width / 2
        cy = height / 2


        if isinstance(mesh, Mesh):
            faces = mesh.faces
            vertices = mesh.vertices

        for i1, i2, i3, char in faces:
            v1 = vertices[i1]
            v2 = vertices[i2]
            v3 = vertices[i3]
           
            new_v1 = Vector3(int(v1.x * scale * aspect_ratio + cx), int(v1.y * scale + cy), v1.z)
            new_v2 = Vector3(int(v2.x * scale * aspect_ratio + cx), int(v2.y * scale + cy), v2.z)
            new_v3 = Vector3(int(v3.x * scale * aspect_ratio + cx), int(v3.y * scale + cy), v3.z)
           
            proj_mesh.append([new_v1, new_v2, new_v3, char])
        return proj_mesh
    def perspective_proj(self, mesh, width=100, height=30, scale=2, aspect_ratio=2, depth_scale=0.5, default_depth=-10):
            proj_mesh = []
           
            cx = width / 2
            cy = height / 2

            if isinstance(mesh, Mesh):
                faces = mesh.faces
                vertices = mesh.vertices
 
            for i1, i2, i3, char in faces:
                v1 = vertices[i1]
                v2 = vertices[i2]
                v3 = vertices[i3]

                x0_proj = v1.x / (-(v1.z + default_depth) * depth_scale + 1)
                x1_proj = v2.x / (-(v2.z + default_depth) * depth_scale + 1)
                x2_proj = v3.x / (-(v3.z + default_depth) * depth_scale + 1)
                y0_proj = v1.y / (-(v1.z + default_depth) * depth_scale + 1)
                y1_proj = v2.y / (-(v2.z + default_depth) * depth_scale + 1)
                y2_proj = v3.y / (-(v3.z + default_depth) * depth_scale + 1)
               
                new_v1 = Vector3(int(x0_proj * scale * aspect_ratio + cx), int(y0_proj * scale + cy), v1.z)
                new_v2 = Vector3(int(x1_proj * scale * aspect_ratio + cx), int(y1_proj * scale + cy), v2.z)
                new_v3 = Vector3(int(x2_proj * scale * aspect_ratio + cx), int(y2_proj * scale + cy), v3.z)
               
                proj_mesh.append([new_v1, new_v2, new_v3, char])
            return proj_mesh
           