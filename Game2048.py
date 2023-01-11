
# Build 2048 in python using pygame
import pygame
import random

pygame.init()

# Initial set up
WIDTH = 400
HEIGHT = 500
screan = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('2048')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesambold.ttf', 24)


