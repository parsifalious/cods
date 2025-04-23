import pygame
import random
import time
pygame.init()
W=1200
H=850
timing=time.time()
timb=False #to start secoundmeter
clock=pygame.time.Clock()
scr=pygame.display.set_mode((W,H))
lv=1
sh=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snakeh.png") #head
sb=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snakeb.png") #body
st=pygame.transform.rotate(pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snaket.png"),180) #tail

srw=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snake1.png")   #body when it rotates
srd=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snake14.png")
slw=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snake12.png")
sld=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snake13.png")

meat=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/meat.png") #food
gap=pygame.transform.scale(pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/gapple.png"),(40,40))
crab=pygame.transform.scale(pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/crabsb.png"),(40,40)) #great food
food=random.choice((meat,gap,crab)) #random
liof=[sb] #lenth of body

ship=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/shipi.png") #border
lv1=pygame.Surface((1200,850))
lv2=pygame.transform.scale(pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/lvl2.png"),(1200,850))
lv3=pygame.transform.scale(pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/lvl3.png"),(1200,850))  #lvl backgrounds

lv1.fill((0,0,0))
fps=8 #fps
lens=1 #length of body
sur=True #survival of snake
done=True 
x=W/2
y=H/2
k=x
p=y-40
py=True #action to down
px=False #to right
pxl=False #to left
pyw=False #to up
i=0 #amount of rotates
yiu=0
yid=0
xil=0
fi=0
foode=True #exiting of great food

an=0 #angle
rot=False 
rot2=False
rot3=False
rot4=False
pos=[(x,p-40),(k,p)] #positions of parts of body(tail,body)

rx=random.randint(90,1050) 
ry=random.randint(90,710) #meat position
iea=pos[0]
scor=0
f=pygame.font.Font("/Users/alialesov/Desktop/labs/lab8/snake/cartoon.ttf",100)
go=f.render("Game Over", False,(255,255,255))
pon=pygame.font.Font("/Users/alialesov/Desktop/labs/lab8/snake/day.ttf",60)
pres=pon.render("press R to restart",False,(0,0,0))
wer=pygame.font.Font("/Users/alialesov/Desktop/labs/lab8/snake/day.ttf",40)
nex=False #to next lvl
cong=False #WIN
sct=9 #score to go next or win
while done:
    for ev in pygame.event.get():
        if ev.type==pygame.QUIT:
            done=False
        if ev.type==pygame.KEYDOWN:
            if ev.key==pygame.K_r or (nex==True and ev.key==pygame.K_n):
                sur=True
                fi=0
                foode=True
                timb=False
                food=random.choice((meat,gap))
                x=W/2
                y=H/2
                liof=[sb]
                k=x
                p=y-40
                py=True
                px=False
                pxl=False
                pyw=False
                rot=False
                i=0
                rx=random.randint(90,1110)
                ry=random.randint(90,760)
                lens=1
                pos=[(x,p-40),(k,p)]
                sh=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snakeh.png")
                sb=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snakeb.png")
                st=pygame.transform.rotate(pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snaket.png"),180)

                srw=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snake1.png")
                srd=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snake14.png")
                slw=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snake12.png")
                sld=pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/snake13.png")
                iea=pos[0]
                scor=0
                nex=False
                rot2=False
                rot3=False
                rot4=False
    if scor>=sct and lv==1:
        sct=15
        nex=True
        lv+=1
    if scor>=sct and lv==2:
        sct=18
        nex=True
        lv+=1
    if scor>=sct and lv==3:
        cong=True
    
    

    pre=pygame.key.get_pressed()
    if sur==True and nex==False and cong==False:
        if lv==1:
            scr.blit(lv1,(0,0)) 
        elif lv==2:
            scr.blit(lv2,(0,0))
            fps=8 #velocity to 8
        elif lv==3:
            scr.blit(lv3,(0,0))
            fps=8 #velocity to 10
        if py==True:
            
            y+=40 #action for 1 body
        if pyw==True:
            y-=40
        if px==True:
            x+=40
        if pxl==True:
            x-=40
        if i<lens+1:
            liof[i-1]=pygame.transform.rotate(liof[i-1],an)
            yui=liof[i-1]  #rotate body
        
        if pre[pygame.K_DOWN] and (px==True or pxl==True):
            if px==True:
                an=-90
                a1=srd #gebuig body
            else:
                a1=slw
                an=90
            rot=True
            sh=pygame.transform.rotate(sh,an) #rotate head
            yid=0
            py=True
            px=False
            pxl=False
            pyw=False
        if pre[pygame.K_UP] and (px==True or pxl==True):
            if px==True:
                an=90
                a2=srw
            else:
                a2=sld
                an=-90
            rot2=True
            sh=pygame.transform.rotate(sh,an)
            yiu=0
            py=False
            px=False
            pxl=False
            pyw=True
        if pre[pygame.K_RIGHT] and (py==True or pyw==True):
            i=0
            if py==True:
                a=sld
                an=90
            else:
                a=slw
                an=-90
            rot3=True
            sh=pygame.transform.rotate(sh,an)
            py=False
            px=True
            pxl=False
            pyw=False
        if pre[pygame.K_LEFT] and (py==True or pyw==True): 
            if py==True:
                a3=srw
                an=-90
            else:
                a3=srd
                an=90
            rot4=True
            sh=pygame.transform.rotate(sh,an)
            xil=0
            py=False
            px=False
            pxl=True
            pyw=False
        
        if (yid==lens+1 and rot) or (yiu==lens+1 and rot2) or (i==lens+1 and rot3) or (xil==lens+1 and rot4):
            st=pygame.transform.rotate(st,90)

        if rot3==True and i<lens+1 and i>=1:
            if i>1:
                liof[i-2]= pygame.transform.rotate(sb,90)
            ish1=liof[i-1]
            liof[i-1]=a #body-->gebuig body
        elif rot3==True and i>=1:
            liof[i-2]=pygame.transform.rotate(sb,90)
            rot3=False

        if rot==True and yid<lens+1 and yid>=1:
            if yid>1:
                liof[yid-2]=sb
            ish2=liof[yid-1]
            liof[yid-1]=a1 #body-->gebuig body
        elif rot==True and yid>=1:
            liof[yid-2]=sb
            rot=False

        if rot2==True and yiu<lens+1 and yiu>=1:
            if yiu>1:
                liof[yiu-2]=sb
            ish3=liof[yiu-1]
            liof[yiu-1]=a2 #body-->gebuig body
        elif rot2==True and yiu>=1:
            liof[yiu-2]=sb
            rot2=False

        if rot4==True and xil<lens+1 and xil>=1:
            if xil>1:
                liof[xil-2]=pygame.transform.rotate(sb,90)
            ish4=liof[xil-1]
            liof[xil-1]=a3 #body-->gebuig body
        elif rot4==True and xil>=1:
            liof[xil-2]=pygame.transform.rotate(sb,90)
            rot4=False

        if len(pos)>3:
            for g in pos[:-1]:
                if g[0]==x and g[1]==y:
                    sur=False #harakiri function
        
        if timb==True: #timer begining
            timing=time.time()
            timb=False

        if food==crab:
            if time.time()-timing>5.0: #timer process
                timing=time.time()
                foode=False
        if ((x+40>=rx and x<=rx) or (x>=rx and x-40<=rx)) and ((y<=ry and y+40>=ry) or (y>=ry and y-40<=ry)):
            rx=random.randint(90,1050)
            ry=random.randint(90,710)
            for m in pos:
                while (m[0]+40>=rx and m[0]<=rx) or (m[0]>=rx and m[0]-40<=rx) and ((m[1]<=ry and m[1]+40>=ry) or (m[1]>=ry and m[1]-40<=ry)):
                    rx=random.randint(90,1050)
                    ry=random.randint(90,710) #due to it food dont have same position with snake
            
            liof.append(yui) #push rotated body
            pos.insert(0,iea) 
            lens+=1
            if food==meat:
                scor+=1
            elif food==gap:
                scor+=2
            else:
                scor+=4
                fi=0
            if fi!=5:
                food=random.choice((meat,gap))
            else: #to get great food
                food=crab
                timb=True
            fi+=1
        elif food==crab and foode==False: #if time is over
            food=random.choice((meat,gap))
            fi=0
            rx=random.randint(90,1050)
            ry=random.randint(90,710)
            for m in pos:
                while (m[0]+40>=rx and m[0]<=rx) or (m[0]>=rx and m[0]-40<=rx) and ((m[1]<=ry and m[1]+40>=ry) or (m[1]>=ry and m[1]-40<=ry)):
                    rx=random.randint(90,1050)
                    ry=random.randint(90,710)
            foode=True
        sctxt=wer.render(f"score  {scor}",False,"Green")
        scr.blit(ship,(0,0))

        scr.blit(sh,(x,y))
        for j in range(0,len(liof)):
            scr.blit(liof[j],pos[lens-j])
        scr.blit(st,(pos[0]))
        scr.blit(food,(rx,ry))
        scr.blit(sctxt,(550,70))
        scr.blit(wer.render(f"score to next {sct}",False,"Blue"),(510,120))
        scr.blit(wer.render(f"lvl: {lv}",False,"Yellow"),(900,70))
        k=x
        p=y
        iea=pos[0] #save position for tail if there will new part of body
        pos.pop(0) 
        pos.append((k,p))
        i+=1
        yid+=1
        yiu+=1
        xil+=1

        if y<90 or y>710 or x<90 or x>1050:
            sur=False
    elif nex==False and cong==False: #restart window
        pygame.draw.rect(scr,"Red",pygame.Rect(0, 0, W, H))
        scr.blit(go,(400,250))
        scr.blit(pres,(370,400))
    elif cong==False: #next level window
        pygame.draw.rect(scr,"Blue",pygame.Rect(0, 0, W, H))
        scr.blit(wer.render("press n to next lvl",False,"Red"),(300,300))
    else: #win window
        scr.blit(pygame.transform.scale(pygame.image.load("/Users/alialesov/Desktop/labs/lab8/snake/youwin.jpg"),(1200,850)),(0,0))
    pygame.display.update()
    pygame.display.flip()
    clock.tick(fps)