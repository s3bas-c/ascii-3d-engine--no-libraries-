class Screen():
    def __init__(self, width, height):
        self.height = height
        self.width = width
       
        self.default_pixel = " "
        
        self.errors = []
       
        self.screen = [[self.default_pixel for i in range(width)] for i in range(height)]
       
    def render(self, show_errors=True):
        #self.clear_console()
        print("\033[H", end="")
        for i in range(self.height):
            idx = self.height - i - 1
            line = "".join(self.screen[idx])
            print(f". {line}")
        if show_errors == True:
            for i in range(len(self.errors)):
                print(self.errors[i])
        self.errors.clear()

    def clear(self):
        self.screen = [[self.default_pixel for i in range(self.width)] for i in range(self.height)]
        self.errors.clear()
       
    def edit_pixel(self, x, y, char):
        try:
            if x < 0 or y < 0:
                raise IndexError
            self.screen[int(y)][int(x)] = char
        except IndexError:
            self.errors.append(f"ERROR: pixel ({x}, {y}) out of range.")
           
    def clear_pixel(self, x, y):
        try:
            if x < 0 or y < 0:
                raise IndexError
            self.screen[int(y)][int(x)] = self.default_pixel
        except IndexError:
            self.errors.append(f"ERROR: pixel ({x}, {y}) out of range.")

    def draw_line(self, x0, y0, x1, y1, char):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0< y1 else -1
        err = dx - dy

        while True:
            self.edit_pixel(x0, y0, char)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def edge_x(self, p1, p2, y):
        if p1.y == p2.y:
            return p1.x


        t = (y - p1.y) / (p2.y - p1.y)
        return p1.x + t * (p2.x - p1.x)

    def fill_face(self, v1, v2, v3, char):
        points = [v1,v2,v3]


        points = sorted([v1, v2, v3], key=lambda p: p.y, reverse=True)
        top = points[0]
        mid = points[1]
        bottom = points[2]


        for y in range(top.y, bottom.y - 1, -1):
            x1 = self.edge_x(top, bottom, y)


            if y >= mid.y:
                x2 = self.edge_x(top, mid, y)
            else:
                x2 = self.edge_x(mid, bottom, y)


            for x in range(int(min([x1, x2])), int(max([x1, x2]))):
                self.edit_pixel(x, y, char)
 
    def draw_lines(self, mesh, char):
        for v1, v2, v3 in mesh:  
            x0, y0 = v1.x, v1.y
            x1, y1 = v2.x, v2.y
            x2, y2 = v3.x, v3.y


            self.draw_line(x0,y0,x1,y1,char)
            self.draw_line(x1,y1,x2,y2,char)
            self.draw_line(x2,y2,x0,y0,char)


    def calculate_triangle_depth(self,v1,v2,v3):
        return (v1.z + v2.z + v3.z) / 3


    def draw_faces(self, mesh):
        faces = []
        for v1, v2, v3, char in mesh:
            depth = self.calculate_triangle_depth(v1,v2,v3)
            faces.append([depth,v1,v2,v3,char])


        faces.sort(key=lambda x: x[0])
        for depth,v1,v2,v3,char in faces:
            self.fill_face(v1,v2,v3,char)
