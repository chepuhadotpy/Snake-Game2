import pygame
import random
from time import sleep

pygame.init()

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
yellow = (255, 255, 102)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Display settings
dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка')

# Variables
snake_list = []
snake_pos = [dis_width / 2, dis_height / 2]
move_direction = 'RIGHT'
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()
font_style = pygame.font.SysFont('Comic Sans MS', 40)
score_font = pygame.font.SysFont('Times New Roman', 24)

def message(msg, color, dest):
    mssg = font_style.render(msg, False, color)
    dis.blit(mssg, dest)
    pygame.display.update()

def show_score(score):
    value = score_font.render("Your score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def draw_snake(snake_list):
    for pos in snake_list:
        pygame.draw.rect(dis, black, [pos[0], pos[1], snake_block, snake_block])

def game_close():
    message('You lose!', red, [dis_width/2.5, dis_height/2.5])
    message('Press Z to exit or X to restart', red, [dis_width/6, dis_height/2])
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_x:
                    game_loop()
                    return

def game_loop():
    global move_direction

    snake_list.clear()
    snake_list.append(list(snake_pos))
    length_of_snake = 1
    score = 0

    food = (round(random.randrange(0, dis_width - snake_block) / 10) * 10,
            round(random.randrange(0, dis_height - snake_block) / 10) * 10)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                message('Bye', black, [dis_width/2.5, dis_height/2.5])
                sleep(3)
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and move_direction != 'RIGHT':
                    move_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and move_direction != 'LEFT':
                    move_direction = 'RIGHT'
                elif event.key == pygame.K_UP and move_direction != 'DOWN':
                    move_direction = 'UP'
                elif event.key == pygame.K_DOWN and move_direction != 'UP':
                    move_direction = 'DOWN'

        snake_pos[0] += (move_direction == 'RIGHT' and snake_block) or (move_direction == 'LEFT' and -snake_block)
        snake_pos[1] += (move_direction == 'DOWN' and snake_block) or (move_direction == 'UP' and -snake_block)

        if snake_pos[0] >= dis_width or snake_pos[0] < 0 or snake_pos[1] >= dis_height or snake_pos[1] < 0:
            message('You lose!', red, [dis_width / 2.5, dis_height / 2.5])
            message("You are a fool, so you can't even restart.", red, [10, dis_height / 2])
            sleep(5)
            pygame.quit()
            quit()

        dis.fill(white)
        pygame.draw.rect(dis, blue, [food[0], food[1], snake_block, snake_block])

        snake_head = [snake_pos[0], snake_pos[1]]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        if any(block == snake_head for block in snake_list[:-1]):
            game_close()

        draw_snake(snake_list)
        show_score(score)
        pygame.display.update()

        if snake_pos[0] == food[0] and snake_pos[1] == food[1]:
            food = (round(random.randrange(0, dis_width - snake_block) / 10) * 10,
                    round(random.randrange(0, dis_height - snake_block) / 10) * 10)
            length_of_snake += 1
            score += 1

        clock.tick(snake_speed)


game_loop()