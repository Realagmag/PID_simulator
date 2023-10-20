import pygame
from utils import rotate_center
import math

class AbstractCar:
    def __init__(self, velocity):
        START_POS = (80 , 180)
        LEFT_IMG = pygame.image.load("images/robot.png")
        RIGHT_IMG = pygame.image.load("images/robot.png")

        self.vel = velocity
        self.angle = 180
        self.left_sensor_img = LEFT_IMG
        self.right_sensor_img = RIGHT_IMG
        for x in range(int(self.left_sensor_img.get_width()/2), self.left_sensor_img.get_width()):
            for y in range(self.left_sensor_img.get_height()):
                self.left_sensor_img.set_at((x,y), (0,0,0,0))
        for x in range(int(self.right_sensor_img.get_width()/2)):
            for y in range(self.right_sensor_img.get_height()):
                self.right_sensor_img.set_at((x,y), (0,0,0,0))
        self.x, self.y = START_POS
            
    def draw(self, win):
        left_rotated_image, new_rect = rotate_center(win, self.left_sensor_img, (self.x, self.y), self.angle)
        self.left_mask = pygame.mask.from_surface(left_rotated_image)
        win.blit(left_rotated_image, new_rect)
        right_rotated_image, new_rect = rotate_center(win, self.right_sensor_img, (self.x, self.y), self.angle)
        self.right_mask = pygame.mask.from_surface(right_rotated_image)
        win.blit(right_rotated_image, new_rect)
        
    def move_forward(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel
        self.x -= horizontal
        self.y -= vertical
        
    def calculate_error(self, mask, x=0, y=0):
        offset = (int(self.x - x), int(self.y - y))
        overlapped_left = mask.overlap_mask(self.left_mask, offset)
        overlapped_right = mask.overlap_mask(self.right_mask, offset)
        return overlapped_left, overlapped_right
    
    def change_angle(self, change_in_angle):
        if self.angle + change_in_angle > 360:
            self.angle = (self.angle + change_in_angle)%360
        elif self.angle + change_in_angle < 0:
            self.angle += change_in_angle
            while not self.angle >= 0:
                self.angle += 360
        else:
            self.angle += change_in_angle
            