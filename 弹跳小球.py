import pygame
from pygame.locals import *
import sys

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("弹跳小球游戏")

ball_radius = 50
ball_color = (255,0 , 0)
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 0  # Initialize the speed to zero
ball_speed_y = 0  # Initialize the speed to zero

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Event handling for arrow keys
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                ball_speed_x = -20  # Move left
            elif event.key == K_RIGHT:
                ball_speed_x = 20   # Move right
            elif event.key == K_UP:
                ball_speed_y = -20  # Move up
            elif event.key == K_DOWN:
                ball_speed_y = 20   # Move down
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                ball_speed_x = 0  # Stop horizontal movement
            if event.key == K_UP or event.key == K_DOWN:
                ball_speed_y = 0  # Stop vertical movement

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius < 0 or ball_x + ball_radius > screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius < 0 or ball_y + ball_radius > screen_height:
        ball_speed_y = -ball_speed_y

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
