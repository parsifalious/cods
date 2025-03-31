import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((940, 680))
    clock = pygame.time.Clock()
    
    radius = 7
    x = 0
    y = 0
    mode = 'blue'
    points = []
    dr=False
    iop=False
    uuu=False
    drtype=1
    recst=False
    ior=False
    fix1=False
    drr=False
    zero=False #to zero the vatribles
    gp=[(0,0),(0,0),(0,0)]
    dp=[(0,0),(0,0),(0,0)]
    rp=[(0,0),(0,0),(0,0)]
    rpg=[(0,0),(0,0),(0,0)]
    opg=[(0,0),(0,0),(0,0)] #for polygons
    rs=[]
    pos=(0,0)
    recp=pygame.Surface((0,0)) #for figures
    recpc=pygame.Surface((0,0))
    recpb=pygame.Surface((0,0))
    f=pygame.font.Font("/Users/alialesov/Desktop/labs/lab8/snake/day.ttf",15)
    pp=pygame.font.Font("/Users/alialesov/Desktop/labs/lab8/snake/day.ttf",25)
    pres=pp.render("PRESS",False,"White")
    tor=f.render("1 to RED",False,(255,255,255))
    tog=f.render("2 to GREEN",True,(255,255,255))
    tob=f.render("3 to BLUE",False,(255,255,255))
    toe=f.render("e to eraser",False,(255,255,255))
    top=f.render("p to plus radius",False,(255,255,255))
    tom=f.render("m to minus radius",False,(255,255,255))
    topai=f.render("a to painting",False,(255,255,255))
    torec=f.render("r to rectangle",False,(255,255,255))
    toc=f.render("c to circle",False,(255,255,255))
    tod=f.render("mouseL to draw",False,(255,255,255))
    tos=f.render("s to square",False,(255,255,255))
    tot=f.render("t to right triangle",False,(255,255,255))
    tol=f.render("l to equilateral triangle",False,(255,255,255))
    tov=f.render("v to romb",False,(255,255,255))
    presit=[tor,tog,tob,toe,top,tom,topai,torec,toc,tod,tos,tot,tol,tov]

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_KP_1 or event.key == pygame.K_1:
                    mode = 'red'
                elif event.key == pygame.K_2 or event.key == pygame.K_KP_2 :
                    mode = 'green'
                elif event.key == pygame.K_3 or event.key == pygame.K_KP_3:
                    mode = 'blue'
                if event.key==pygame.K_e:
                    mode = "black"
                if event.key==pygame.K_p:
                    radius = min(200, radius + 1)
                if event.key == pygame.K_m: 
                    radius = max(1, radius - 1)

                #draw type(rect,circle,painting...)
                if event.key==pygame.K_a:
                    drtype=1
                elif event.key==pygame.K_r:
                    drtype=2
                    zero=True
                elif event.key==pygame.K_c:
                    drtype=3
                    zero=True
                elif event.key==pygame.K_s:
                    drtype=4
                    zero=True
                elif event.key==pygame.K_t:
                    drtype=5
                    zero=True
                elif event.key==pygame.K_l:
                    drtype=6
                    zero=True
                elif event.key==pygame.K_v:
                    drtype=7
                    zero=True

            if zero==True:
                recst=False
                ior=False
                fix1=False
                drr=False
                pos2=(0,0)
                recp=pygame.Surface((0,0))
                zero=False

            if drtype==1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1 and iop==False:
                        dr=True
                        iop=True
                    elif event.button == 1 :
                        dr=False
                        iop=False
                        uuu=True
                    
                

                if event.type == pygame.MOUSEMOTION and dr==True:
                    # if mouse moved, add point to list
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                    if len(points)>2:
                        points.pop(0)
                elif event.type == pygame.MOUSEMOTION and uuu==True:
                    points.pop(0)
                    points.pop(0)
                    uuu=False
            if drtype!=1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if event.button == 1 and ior==False:
                        fix1=True
                        recst=True
                        ior=True
                    elif event.button == 1:
                        rs.append((recp,pos))
                        recp=pygame.Surface((0,0))
                        recst=False
                        ior=False
                        drr=False

                if recst==True:
                    if event.type == pygame.MOUSEMOTION:
                        if fix1==True:
                            drr=True
                            pod1=event.pos
                            fix1=False
                        pod=event.pos
            
                    
            #screen.fill((0, 0, 0))
            
            # draw all points
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        if drtype!=1 and drr==True:
            if abs(pod1[0]-pod[0])>=abs(pod1[1]-pod[1]):
                scuw=abs(pod1[1]-pod[1])

            else:
                scuw=abs(pod1[0]-pod[0])
            pos2=pos
            if pod[0]<pod1[0] and pod[1]<pod1[1]:
                dp=[(abs(pod1[0]-pod[0]),abs(pod1[1]-pod[1])),(abs(pod1[0]-pod[0]),0),(0,0)]
                if drtype==4 or drtype==6:
                    pos=(pod1[0]-scuw,pod1[1]-scuw)
                else:
                    pos=pod
                rp=((0,0),(scuw,0),(scuw/2,scuw))
                
            elif pod[0]<pod1[0] and pod[1]>pod1[1]:
                dp=[(abs(pod1[0]-pod[0]),0),(abs(pod1[0]-pod[0]),abs(pod1[1]-pod[1])),(0,abs(pod1[1]-pod[1]))]
                if drtype==4 or drtype==6:
                    pos=(pod1[0]-scuw,pod1[1])
                else:
                    pos=(pod[0],pod1[1])
                rp=((scuw/2,0),(0,scuw),(scuw,scuw))
                
            elif pod[0]>pod1[0] and pod[1]<pod1[1]:
                dp=[(0,0),(0,abs(pod1[1]-pod[1])),(abs(pod1[0]-pod[0]),0)]
                if drtype==4 or drtype==6:
                    pos=(pod1[0],pod1[1]-scuw)
                else:
                    pos=(pod1[0],pod[1])
                rp=((0,0),(scuw,0),(scuw/2,scuw))
            else:
                dp=[(0,0),(0,abs(pod1[1]-pod[1])),(abs(pod1[0]-pod[0]),abs(pod1[1]-pod[1]))]
                pos=pod1
                rp=((scuw/2,0),(0,scuw),(scuw,scuw))
            for x in rs:
                screen.blit(x[0],(x[1]))
            recpb=recp
        if drtype==2 and drr==True:
            recp=pygame.Surface((abs(pod1[0]-pod[0]),abs(pod1[1]-pod[1])))
            recpb.fill((0,0,0))
            recp.fill(mode)
            screen.blit(recpb,(pos2))
            screen.blit(recp,(pos))
            
        if drtype==3 and drr==True:
            recp=pygame.Surface((abs(pod1[0]-pod[0]),abs(pod1[1]-pod[1])),pygame.SRCALPHA)
            recpb.fill((0,0,0,0))
            pygame.draw.ellipse(recpb,"Black",((0,0),(recpb.get_width(),recpb.get_height())))
            pygame.draw.ellipse(recp,mode,((0,0),(abs(pod1[0]-pod[0]),abs(pod1[1]-pod[1]))))
            screen.blit(recpb,(pos2))
            screen.blit(recp,(pos))

        if drtype==4 and drr==True:
            recp=pygame.Surface((abs(scuw),abs(scuw)))
            recpb.fill((0,0,0))
            recp.fill(mode)
            screen.blit(recpb,(pos2))
            screen.blit(recp,(pos))
        if drtype==5 and drr==True:
            recp=pygame.Surface((abs(pod1[0]-pod[0]),abs(pod1[1]-pod[1])),pygame.SRCALPHA)
            recpb.fill((0,0,0,0))
            pygame.draw.polygon(recpb,(0,0,0),gp,0)
            pygame.draw.polygon(recp,mode,dp,0)
            gp=dp
            screen.blit(recpb,(pos2))
            screen.blit(recp,(pos))
        if drtype==6 and drr==True:
            recp=pygame.Surface((abs(scuw),abs(scuw)),pygame.SRCALPHA)
            recpb.fill((0,0,0,0))
            pygame.draw.polygon(recpb,"Black",rpg,0)
            pygame.draw.polygon(recp,mode,rp,0)
            rpg=rp
            screen.blit(recpb,(pos2))
            screen.blit(recp,(pos))
        if drtype==7 and drr==True:
            recp=pygame.Surface((abs(pod1[0]-pod[0]),abs(pod1[1]-pod[1])),pygame.SRCALPHA)
            ox=abs(pod1[0]-pod[0])
            oy=abs(pod1[1]-pod[1])
            recpb.fill((0,0,0,0))
            op=[(ox/2,0),(ox,oy/2),(ox/2,oy),(0,oy/2)]
            pygame.draw.polygon(recpb,"Black",opg,0)
            pygame.draw.polygon(recp,mode,op,0)
            opg=op
            screen.blit(recpb,(pos2))
            screen.blit(recp,(pos))


        ypr=60
        screen.blit(pres,(770,10))
        for x in presit:
            screen.blit(x,(800,ypr)) 
            ypr+=20
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = "Blue"
    elif color_mode == 'red':
        color = "Red"
    elif color_mode == 'green':
        color = "Green"
    elif color_mode == "black":
        color=(0,0,0)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)





main()