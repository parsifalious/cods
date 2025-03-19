import pygame as pg
import sys
pg.init()
pg.mixer.init()
playlist=["HBA.MP3","ALL RED.mp3","SKELETONS.MP3","2024.mp3"]
track=0
VOLUME=0.5

background_image=pg.image.load("MUSIC.png")
background_image=pg.transform.scale(background_image,(500,500))
def play_music():
    global track
    pg.mixer.music.load(playlist[track])
    pg.mixer.music.play()

play_music()

screen=pg.display.set_mode((500,500))
pg.display.set_caption("Music Player")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()


        if event.type==pg.KEYDOWN:
            if event.key==pg.K_RIGHT:
                track=(track+1)%len(playlist)
                play_music()
            elif event.key==pg.K_LEFT:
                track=(track-1)%len(playlist)
                play_music()
            elif event.key==pg.K_SPACE:
                if pg.mixer.music.get_busy():
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()
            elif event.key==pg.K_DOWN:
                VOLUME = max(VOLUME - 0.1, 0.0)
                pg.mixer.music.set_volume(VOLUME)
            elif event.key==pg.K_UP:
                VOLUME = min(VOLUME + 0.1, 1.0)
                pg.mixer.music.set_volume(VOLUME)
            elif event.key==pg.K_s:
                pg.mixer.music.stop()
    screen.blit(background_image,(0,0))
    pg.display.flip()

