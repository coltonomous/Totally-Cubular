import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)

colors = {"white": (255, 255, 255), "black": (0, 0, 0), "red": (255, 0, 0), "green": (0, 255, 0),
          "blue": (0, 0, 255), "yellow": (255, 255, 0), "magenta": (255, 0, 255), "cyan": (0, 255, 255),
          "darkRed": (175, 0, 0), "darkGreen": (0, 175, 0), "brown": (101, 67, 33), "grey": (125, 125, 125)}

def draw_cube():
    glBegin(GL_QUADS)

    colors_list = list(colors.keys())
    for surface in surfaces:
        index = 0
        for vertex in surface:
            index += 1
            glColor3fv(colors[colors_list[index]])
            glVertex3fv(vertices[vertex])

    glEnd()

    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])

    glEnd()

def main():
    pygame.init()
    gameDisplay = (800, 600)
    pygame.display.set_mode(gameDisplay, DOUBLEBUF | OPENGL)

    gluPerspective(45, (gameDisplay[0] / gameDisplay[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -40.0)
    glRotatef(0, 0, 0, 0)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslate(0.75, 0, 0)
                elif event.key == pygame.K_RIGHT:
                    glTranslate(-0.75, 0, 0)
                elif event.key == pygame.K_UP:
                    glTranslate(0, -0.6, 0)
                elif event.key == pygame.K_DOWN:
                    glTranslate(0, 0.75, 0)

            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         glTranslate(0, 0, 1)
            #     elif event.button == 5:
            #         glTranslate(0, 0, -1)


        # glRotatef(1, 3, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glTranslate(0, 0, 0.1)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()
    quit()

main()
