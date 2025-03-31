import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import wireCube
import time
pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (97, 0, 153, 0)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')


def initialise():
    glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
    glColor(drawing_color)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # modelview
    glMatrixMode(GL_MODELVIEW)
    glTranslate(0, 0, -5)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)
    glTranslate(0, 0, -2)

rotation_angle_x = 0.0  
rotation_angle_y = 0.0  
rotation_speed = 90.0   


position_x = 0.0  
position_y = 0.0  
movement_speed = 2.0  

scale = 1.0  
scaling_speed = 0.5  

# Time tracking
last_time = time.time()


done = False
initialise()
while not done:
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        rotation_angle_x -= rotation_speed * delta_time
    if keys[pygame.K_DOWN]:
        rotation_angle_x += rotation_speed * delta_time  
    if keys[pygame.K_LEFT]:
        rotation_angle_y -= rotation_speed * delta_time   
    if keys[pygame.K_RIGHT]:
        rotation_angle_y += rotation_speed * delta_time 
    if keys[pygame.K_w]:
        position_y += movement_speed * delta_time
    if keys[pygame.K_s]:
        position_y -= movement_speed * delta_time  
    if keys[pygame.K_a]:
        position_x -= movement_speed * delta_time  
    if keys[pygame.K_d]:
        position_x += movement_speed * delta_time  
    if keys[pygame.K_q]:
        scale += scaling_speed * delta_time  
    if keys[pygame.K_e]:
        scale -= scaling_speed * delta_time
        if scale < 0.1:
            scale = 0.1

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )

   
    glPushMatrix()
    glScalef(1.0, -1.0, 1.0)  
    glTranslatef(position_x, -position_y - 1, 0)  
    glScalef(scale, scale, scale)  
    glRotatef(rotation_angle_x, 1, 0, 0)  
    glRotatef(rotation_angle_y, 0, 1, 0)
    glColor4f(1.0, 1.0, 1.0, 0.5)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    wireCube()
    glDisable(GL_BLEND)
    glPopMatrix()

    
    glPushMatrix()
    glScalef(scale, scale, scale) 
    glTranslatef(position_x, position_y, 0)  
    glRotatef(rotation_angle_x, 1, 0, 0)  
    glRotatef(rotation_angle_y, 0, 1, 0)  
    glColor3f(1.0, 1.0, 1.0)  
    wireCube()
    glPopMatrix()

    pygame.display.flip()
pygame.quit()
