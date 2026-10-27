import pygame
import random

#randow dot position and velocity genarator
def gendot():
    x_int=random.randint(25,825)
    y_int=random.randint(25,400)
    if(x_int>=375):
        x_vel=random.uniform(-20,-25)
    else:
        x_vel=random.uniform(20,25)
    y_vel=random.uniform(-2,2)
    int_pos=[float(x_int),float(y_int)]
    return {"pos":int_pos,"x_vel":x_vel,"y_vel":y_vel,"trail":[]}

pygame.init()

screen=pygame.display.set_mode((850,750))
pygame.display.set_caption('SimEngine.V0.1')

#predefined variables
g=9.80665
t=1/60
white=(255,255,255)
gray=(100,100,100)
black=(0,0,0)
green=(0,55,0)
red=(255,0,0)
orange=(255,165,0)
predicted_x_vel=[]


hit_count=0
dots=[]
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                dot=gendot()
                print(f'dot intiation at{str(dot['pos'])} with {dot["x_vel"]} horizontal velocity and {dot["y_vel"]} vertical velocity')
                dots.append(dot)
                print(type(dots[0]['pos']))
    screen.fill(black)

    #draw border lines
    pygame.draw.line(screen,white,(0,25),(850,25),width=1)
    pygame.draw.line(screen,white,(0,725),(850,725),width=1)
    pygame.draw.line(screen,white,(25,0),(25,750),width=1)
    pygame.draw.line(screen,white,(825,0),(825,750),width=1)

    #draw grid lines
    for i in range(75,725,50):
        pygame.draw.line(screen,green,(25,i),(825,i),width=1)
    for i in range(75,825,50):
        pygame.draw.line(screen,green,(i,25),(i,725),width=1)
    
    #draw radial lines
    for i in range(50,450,50):
        pygame.draw.circle(screen,green,(425,725),i,width=1)
    
    #draw fixed dot
    #pygame.draw.circle(screen,red, (400, 300), 5)

    #draw random dots and make them go in projectile path
    for active_dot in dots:

        

        #draw current position by red dot
        pygame.draw.circle(screen,red,active_dot['pos'],3,width=0)
        x_pos=active_dot['pos'][0]+active_dot['x_vel']*(t)
        y_pos=active_dot['pos'][1]+active_dot["y_vel"]*t+0.5*g*t**2
        active_dot['y_vel']=active_dot['y_vel']+t*g
        active_dot['pos']=[x_pos,y_pos]

        #draw trails
        active_dot['trail'].append(active_dot['pos'])
        #if len(active_dot['trail'])>150:
        #    del active_dot['trail'][0]
        for trail_pixels in active_dot['trail']:
            pygame.draw.circle(screen,orange,trail_pixels,1)
            #print(trail_pixels)
            # screen.set_at(trail_pixels,white)
        #print(type(active_dot['pos']))

        
        #hit counter
        if active_dot['pos'][1]>=725:
            dots.remove(active_dot)
            print('hit at :',active_dot['pos'])
            hit_count+=1
            print('hit count : ',hit_count)
            break

        #path predicting logic
        
    pygame.display.flip()
    clock.tick(60)
pygame.quit()