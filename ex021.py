# Tocando mp3
import pygame as pg
pg.mixer.init()
pg.mixer.music.load('hangloose.mp3')
pg.mixer.music.play()
input()
# pg.event.wait()
