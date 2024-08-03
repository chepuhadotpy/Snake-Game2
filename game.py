import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 500
dis_high = 400
dis = pygame.display.set_mode((dis_width, dis_high))
pygame.display.update()
pygame.display.set_caption('Змейка')

game_over = False
xy = [dis_width/2, dis_high/2]    #  X and Y
clock = pygame.time.Clock
snake_speed = 15
font_style = pygame.font.SysFont('Comic Sans MS', 50)

def message(msg, color):
    mssg = font_style.render(msg, True, color)
    dis.blit(mssg, [dis_width/2, dis_high/2])


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xy[0] -= 10
            elif event.key == pygame.K_RIGHT:
                xy[0] += 10
            elif event.key == pygame.K_UP:
                xy[1] -= 10
            elif event.key == pygame.K_DOWN:
                xy[1] += 10
        else:
            print(event)

    if xy[0] >= dis_width or xy[0] <= 0 or xy[1] >= dis_high or xy[1] <= 0:
        game_over = True

    dis.fill(white)

    pygame.draw.rect(dis, red, [xy[0], xy[1], 10, 10])
    pygame.display.update()
pygame.quit()
quit()