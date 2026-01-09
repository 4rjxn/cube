import pygame as pg

FPS = 60
SCF = 200
pg.init()
screen = pg.display.set_mode((700, 700))
screen.fill(pg.Color("black"))

def project(x,y,z) -> tuple[float,float ]:
    x,y = x/z,y/z
    return (x,y)

def line(Spos,Epos):
    x1,y1 = project(*Spos)
    x2,y2 = project(*Epos)
    dim=pg.display.get_window_size();
    x1,y1=((x1+1)/2)*dim[0],((1-y1)/2)*dim[1]
    x2,y2=((x2+1)/2)*dim[0],((1-y2)/2)*dim[1]
    pg.draw.line(surface=screen,color=pg.Color("green"),start_pos=(x1,y1),end_pos=(x2,y2));
def place(x,y,z):
    x,y = project(x,y,z)
    dim=pg.display.get_window_size();
    x,y=((x+1)/2)*dim[0],((1-y)/2)*dim[1]
    pg.draw.rect(surface=screen,rect=(x,y,10,10),color=pg.Color("green"))

points =[ [1, 1, 3],   # front top right
    [-1, 1, 3],  # front top left
    [-1, -1, 3], # front bottom left
    [1, -1, 3],  # front bottom right
    [1, 1, 5],  # back top right
    [-1, 1, 5], # back top left
    [-1, -1, 5],# back bottom left
    [1, -1, 5.0] ] # back bottom righ


faces = [
    [points[0],points[1],points[2],points[3]],
    [points[4],points[5],points[6],points[7]],
    [points[0],points[1],points[5],points[4]],
    [points[2],points[3],points[7],points[6]],
    [points[3],points[0],points[4],points[7]],
    [points[2],points[1],points[5],points[6]],
         ]


clock = pg.time.Clock()
while True:
    faces = [
        [points[0],points[1],points[2],points[3]],
        [points[4],points[5],points[6],points[7]],
        [points[0],points[1],points[5],points[4]],
        [points[2],points[3],points[7],points[6]],
        [points[3],points[0],points[4],points[7]],
        [points[2],points[1],points[5],points[6]],
             ]
    for event in pg.event.get():
        if(event.type == pg.KEYDOWN):
            if(event.key == pg.K_UP):
                for p in points:
                    p[2] += 0.2;
            if(event.key == pg.K_DOWN):
                for p in points:
                    p[2] -= 0.2;
            if(event.key == pg.K_LEFT):
                for p in points:
                    p[0] -= 0.2;
            if(event.key == pg.K_RIGHT):
                for p in points:
                    p[0] += 0.2;
                
    screen.fill(pg.Color("black"))
    for f in faces:
        line(f[0],f[1])
        line(f[1],f[2])
        line(f[2],f[3])
        line(f[3],f[0]) 
    #for p in points:
    #    p[2] += .5;
    pg.display.update() 
    clock.tick(FPS)






