from OpenGL.GL import *

vertices = [(0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, -0.5, -0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (-0.5, 0.5, -0.5),
            (-0.5, -0.5, -0.5),
            (0.5, -0.5, -0.5),
            (0.5, 0.5, -0.5),
            (0.5, 0.5, 0.5),
            (0.5, -0.5, 0.5)
            ]
triangles = [0, 2, 3, 0, 3, 1, 8, 4, 5, 8, 5, 9, 10, 6, 7, 10, 7, 11, 12,
             13, 14, 12, 14, 15, 16, 17, 18, 16, 18, 19, 20, 21, 22, 20, 22, 23]

def wireCube():
    for t in range(len(triangles) - 3):
        glBegin(GL_LINES)
        glVertex3fv(vertices[triangles[t]])
        glVertex3fv(vertices[triangles[t + 1]])
        glVertex3fv(vertices[triangles[t + 2]])
        glEnd()
        t += 3

    
    center = [sum(coord) / len(vertices) for coord in zip(*vertices)]

    
    scale_factor = 0.1
    smaller_cube_vertices = [
        [(v[i] - center[i]) * scale_factor + center[i] for i in range(3)]
        for v in vertices
    ]

    
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    for t in range(0, len(triangles), 4):
        for i in range(4):
            glVertex3fv(smaller_cube_vertices[triangles[t + i]])
    glEnd()


    glPushMatrix()
    glScalef(1.0, -1.0, 1.0)


    for t in range(len(triangles) - 3):
        glBegin(GL_LINES)
        glVertex3fv(vertices[triangles[t]])
        glVertex3fv(vertices[triangles[t + 1]])
        glVertex3fv(vertices[triangles[t + 2]])
        glEnd()
        t += 3

    
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    for t in range(0, len(triangles), 4):  
        for i in range(4):
            glVertex3fv(smaller_cube_vertices[triangles[t + i]])
    glEnd()

    glPopMatrix()
