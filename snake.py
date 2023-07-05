#import the pygame library
import pygame
import time
import random
 
#intialize the pygame function
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
#1. Set dis_width eqaul to 600
dis_width = 600
#2.Set dis_height eqaul to 400
dis_height = 400 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
#3.Set snake_block eqaul to 10
snake_block = 10
#4.Set snake_speed eqaul to 15
snake_speed = 15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
#5.create a function named our_snake that holds two parameters(snake_block, snake_list)
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
#6.create a function named message that holds two parameters(msg, color)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
#7.create a function named gameLoop
def gameLoop():
    game_over = False
    game_close = False
 
    #8. set x1 equal to dis_width divide by 2
    x1 = dis_width/2
    #9.set y1 equal to dis_height divide by 2
    y1 = dis_height/2
    #10.set x1_change equal to 0
    x1_change = 0
    #11.set y1_change equal to 0
    y1_change = 0
    #12.set snake_List equal to an empty array/list
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            #13.pass Length_of_snake -1 to the function Your_score
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #14.create an if statement for event.key equal equal to pygame.KEYDOWN
                    if event.key == pygame.KEYDOWN:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            #15.create an if statement for event.key equal equal to pygame.QUIT
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        #16. pass x1 to snake_Head.append
        snake_Head.append(x1)
        #17. pass y1 to snake_Head.append
        snake_Head.append(y1)
        #18. pass snake_Head to snake_List.append
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    #quit the pygame
    pygame.quit()
    sys.exit()
    quit()
 
 
gameLoop()
