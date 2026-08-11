from .math3d import Vector3
import copy

class Light3D():
    def directional_light_prediction(self, mesh, direction = [-1, -1, -1], shades="_.,:;+/|#%@"): #_.,:;+/|%#@"
        dx = direction[0]
        dy = direction[1]
        dz = direction[2]
        direction = Vector3(dx, dy, dz).normalize()
        light_mesh = copy.deepcopy(mesh)
        light_mesh.clear_faces()
        for i1, i2, i3, char in mesh.faces:
            v1 = mesh.vertices[i1]
            v2 = mesh.vertices[i2]
            v3 = mesh.vertices[i3]


            edge1 = v2 - v1
            edge2 = v3 - v1
            normal = edge1.cross(edge2).normalize()


            normal = edge1.cross(edge2).normalize()


            face_center = (v1 + v2 + v3) / 3
            outward = face_center - mesh.pivot


            if normal.dot(outward) > 0:
                normal = normal * -1


            brightness = max(0,normal.dot(direction))
            new_char = shades[int(brightness * (len(shades) - 1))]
            light_mesh.set_face(i1,i2,i3,new_char)
        return light_mesh
           
