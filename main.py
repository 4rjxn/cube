import pygame as pg
import math
import god as loader

points = loader.points
faces = loader.faces

FPS = 60
pg.init()
screen = pg.display.set_mode((700, 700))
screen.fill(pg.Color("black"))

def project(x,y,z) -> tuple[float,float ]:
    if z == 0:
        return (0,0)
    x,y = x/z,y/z
    return (x,y)

def rotate(x,y,z,ang):
    c = math.cos(ang)
    s = math.sin(ang)
    x0,z0=x,z 
    x = x0*c+z0*s
    z = x0*s-z0*c
    return (x,y,z)


def line(st,ed):
    dim=pg.display.get_window_size();
    x1,y1 = st[0],st[1]
    x2,y2 = ed[0],ed[1]
    x1pos,y1pos=(x1+1)/2*dim[0],(1-y1)/2*dim[1]
    x2pos,y2pos=(x2+1)/2*dim[0],(1-y2)/2*dim[1]
    pg.draw.line(surface=screen,color=pg.Color("green"),start_pos=(x1pos,y1pos),end_pos=(x2pos,y2pos));
angle = 0
def place(x,y):
    #x,y,z = rotate(x,y,z,angle)
    dim=pg.display.get_window_size();
    x,y=((x+1)/2)*dim[0],((1-y)/2)*dim[1]
    pg.draw.rect(surface=screen,rect=(x,y,10,10),color=pg.Color("green"))


#points = [
#    # ---- TOP ----
#    [ 0.0,  0.55,  0.0],    # 0 top point
#
#    # ---- CROWN RING ----
#    [ 0.18,  0.25,  0.0],   # 1
#    [-0.18,  0.25,  0.0],   # 2
#    [ 0.0,   0.25,  0.18],  # 3
#    [ 0.0,   0.25, -0.18],  # 4
#
#    # ---- GIRDLE (widest part) ----
#    [ 0.35,  0.0,  0.0],    # 5
#    [-0.35,  0.0,  0.0],    # 6
#    [ 0.0,   0.0,  0.35],   # 7
#    [ 0.0,   0.0, -0.35],   # 8
#
#    # ---- PAVILION RING ----
#    [ 0.18, -0.25,  0.0],   # 9
#    [-0.18, -0.25,  0.0],   # 10
#    [ 0.0,  -0.25,  0.18],  # 11
#    [ 0.0,  -0.25, -0.18],  # 12
#
#    # ---- BOTTOM ----
#    [ 0.0, -0.55,  0.0],    # 13 bottom point
#]
#
#faces = [
#    #top face
#    [0, 1, 3],
#    [0, 3, 2],
#    [0, 2, 4],
#    [0, 4, 1],
#    #gradle faces
#    [1, 5, 7],
#    [1, 7, 3],
#    [3, 7, 6],
#    [3, 6, 2],
#    [2, 6, 8],
#    [2, 8, 4],
#    [4, 8, 5],
#    [4, 5, 1],
#    #gradle pacilion
#    [5, 9, 11],
#    [5, 11, 7],
#    [7, 11, 10],
#    [7, 10, 6],
#    [6, 10, 12],
#    [6, 12, 8],
#    [8, 12, 9],
#    [8, 9, 5],
#    #bottom
#    [13, 11, 9],
#    [13, 10, 11],
#    [13, 12, 10],
#    [13, 9, 12]
#]




#points = [
#    [ 0.0,  0.45,  0.0],   # 0 top (elongated)
#    [ 0.0, -0.45,  0.0],   # 1 bottom
#    [ 0.25,  0.0,  0.0],   # 2 right
#    [-0.25,  0.0,  0.0],   # 3 left
#    [ 0.0,  0.0,  0.18],   # 4 front (slightly compressed)
#    [ 0.0,  0.0, -0.18],   # 5 back
#]
#
#faces = [
#    # top half
#    [0, 2, 4],
#    [0, 4, 3],
#    [0, 3, 5],
#    [0, 5, 2],
#
#    # bottom half
#    [1, 4, 2],
#    [1, 3, 4],
#    [1, 5, 3],
#    [1, 2, 5],
#]


#points = [
#    [ 0.0,  0.25,  0.0],   # 0 top
#    [ 0.0, -0.25,  0.0],   # 1 bottom
#    [ 0.25,  0.0,  0.0],   # 2 right
#    [-0.25,  0.0,  0.0],   # 3 left
#    [ 0.0,  0.0,  0.25],   # 4 front
#    [ 0.0,  0.0, -0.25],   # 5 back
#]
#faces = [
#    # top half
#    [0, 2, 4],
#    [0, 4, 3],
#    [0, 3, 5],
#    [0, 5, 2],
#
#    # bottom half
#    [1, 4, 2],
#    [1, 3, 4],
#    [1, 5, 3],
#    [1, 2, 5],
#]


#points = [
# [0.25, 0.25, 0.25],   # front top right
# [-0.25, 0.25, 0.25],  # front top left
# [-0.25, -0.25, 0.25],  # front bottom right
# [0.25, -0.25, 0.25], # front bottom left
#
# [0.25, 0.25, -0.25],   # back top right
# [-0.25, 0.25, -0.25],  # back top left
# [-0.25, -0.25, -0.25], # back bottom left
# [0.25, -0.25, -0.25]]  # back bottom right

#faces = [
#    [0,1,2,3],
#    [4,5,6,7],
#    [0,1,5,4],
#    [2,3,7,6],
#    [3,0,4,7],
#    [2,1,5,6]]
#

clock = pg.time.Clock()
dz = 1
ang = math.pi/3
while True:         
    screen.fill(pg.Color("black"))
    angle += 2*math.pi*(1/FPS)
    #dz += 1/FPS
    ang += math.pi*1/FPS
    #for p in points:
    #    x,y,z = rotate(p[0],p[1],p[2],ang)
    #    place(*project(x,y,z+dz))

    for f in faces:
        for i in range(len(f)):
            p1,p2= points[f[i]],points[f[(i+1)%len(f)]]
            x1,y1,z1 = rotate(p1[0],p1[1],p1[2],ang)
            x2,y2,z2 = rotate(p2[0],p2[1],p2[2],ang)
            line(project(x1,y1,z1+dz),project(x2,y2,z2+dz))

    pg.display.update() 
    clock.tick(FPS)


    #for event in pg.event.get():
    #    if(event.type == pg.KEYDOWN):
    #        if(event.key == pg.K_UP):
    #            for p in points:
    #                p[2] += 0.2;
    #        if(event.key == pg.K_DOWN):
    #            for p in points:
    #                p[2] -= 0.2;
    #        if(event.key == pg.K_LEFT):
    #            for p in points:
    #                p[0] -= 0.2;
    #        if(event.key == pg.K_RIGHT):
    #            for p in points:
    #                p[0] += 0.2;



