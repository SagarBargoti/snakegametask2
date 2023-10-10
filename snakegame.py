import pygame
import sys
import random
pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
snake = Snake()
food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            if event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            if event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            if event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")

    snake.move()

    if snake.check_collision(food):
        snake.eat_food()
        food.randomize_position()

    if snake.check_boundary_collision(WIDTH, HEIGHT) or snake.check_self_collision():
        # Handle game over logic here
        pass

    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)

    pygame.display.update()
