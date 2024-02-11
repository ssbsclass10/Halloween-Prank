# This is a python project of halloween
import pygame
from time import sleep #Taking time
pygame.init() #Initializing a class
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN) #black screen 
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play() 
sleep(5)
pygame.mixer.init()
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(1)
image = pygame.image.load('scr.jpg')
window.blit(image, (0,0))
pygame.display.update()
sleep(20)

