from .math3d import Vector3
import math

class Mesh():
    def __init__(self):
        self.vertices = []
        self.faces = []


        self.rotation = Vector3(0,0,0)
        self.position = Vector3(0,0,0)
        self.pivot = Vector3(0,0,0)
    def add_vertex(self,x,y,z):
        self.vertices.append(Vector3(x,y,z))
   
    def set_face(self, v1, v2, v3, char="#"):
            self.faces.append([v1, v2, v3, char])


    def clear_faces(self):
        self.faces.clear()


    def calculate_center(self):
        self.pivot = Vector3(0, 0, 0)


        for v in self.vertices:
            self.pivot = self.pivot + v
        if len(self.vertices) > 0:
            self.pivot = self.pivot / len(self.vertices)


    def rotate(self, x_rot, y_rot, z_rot):
        x_rot = math.radians(x_rot)
        y_rot = math.radians(y_rot)
        z_rot = math.radians(z_rot)
       
        for v, vector in enumerate(self.vertices):
            relative = vector - self.pivot


            # X rotation
            y = relative.y * math.cos(x_rot) - relative.z * math.sin(x_rot)
            z = relative.y * math.sin(x_rot) + relative.z * math.cos(x_rot)
            relative = Vector3(relative.x,y,z)


            # Y rotation
            x = relative.x * math.cos(y_rot) - relative.z * math.sin(y_rot)
            z = relative.x * math.sin(y_rot) + relative.z * math.cos(y_rot)
            relative = Vector3(x,relative.y,z)


            # Z rotation
            x = relative.x * math.cos(z_rot) - relative.y * math.sin(z_rot)
            y = relative.x * math.sin(z_rot) + relative.y * math.cos(z_rot)
            relative = Vector3(x,y,relative.z)


            final_vertex = relative + self.pivot
            self.vertices[v] = final_vertex
