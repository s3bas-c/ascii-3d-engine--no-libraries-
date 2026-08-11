from .mesh import Mesh

class Model_Converter():
    def convert_obj_file(self, file_name):
        mesh = Mesh()
        with open(file_name, 'r') as file:
            file = file.readlines()
            for line in file:
                line = line.strip().split()
                if line[0] == "v":
                    mesh.add_vertex(float(line[1]),float(line[2]),float(line[3]))
                if line[0] == "f":
                    v1 = line[1].split("/")
                    v1 = v1[0]
                    v2 = line[2].split("/")
                    v2 = v2[0]
                    v3 = line[3].split("/")
                    v3 = v3[0]
                    
                    mesh.set_face(int(v1)-1,int(v2)-1,int(v3)-1)
                    if len(line) > 4:
                        v4 = line[4].split("/")
                        v4 = v4[0]
                        mesh.set_face(int(v1)-1,int(v3)-1,int(v4)-1)
        return mesh
