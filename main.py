import pygame
import time
from utils import pid_regulator, rotate_center
from AbstractCar import AbstractCar
from random import randint

pygame.init()
# definiowanie okna gry
TRACK = pygame.image.load("images/track.png")
TRACK_MASK = pygame.mask.from_surface(TRACK)
win = pygame.display.set_mode((1000, 1000))
# wyświetlenie okna gry
pygame.display.set_caption("PID Simulator")
robot = AbstractCar(5)
integral = 0
derivative = 0
last_error = 0
FPS = 60
run = True
clock = pygame.time.Clock()
# pętla główna
while run:
    clock.tick(FPS)
    # obsługa zdarzeń  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((255, 150, 255))
    win.blit(TRACK,(0,0))

    robot.move_forward()
    robot.draw(win)
    left_sensor, right_sensor = robot.calculate_error(TRACK_MASK)
    print(f'Left:{left_sensor.count()} Right:{right_sensor.count()}')
    error = left_sensor.count() - right_sensor.count()
    # error += randint(-5,5)
    derivative = error - last_error
    integral += error
    change_in_angle = pid_regulator(error, integral, derivative)
    robot.change_angle(change_in_angle)
    last_error = error
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        robot.change_angle(1)
    if keys[pygame.K_d]:
        robot.change_angle(-1)
    if keys[pygame.K_w]:
        robot.move_forward()
    # odświeżenie ekranu 
    pygame.display.update()
    
