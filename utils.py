import pygame

def rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft = top_left).center)
    return rotated_image, new_rect
    
def pid_regulator(error, integral, derivative):
    #error = left - right
    Kp = 0.2
    Ki = 0.01
    Kd = 0
    return Kp*error + Ki*integral + Kd*derivative