import pygame
import os
import random

pygame.mixer.init()
pygame.init()

screen_width =900
screen_height =600
gamewindow = pygame.display.set_mode((screen_width,screen_height))
# title of game
pygame.display.set_caption("Snake eating food")
pygame.display.update()

# images
script_dir = os.path.dirname(os.path.abspath(__file__))
stimg = os.path.join(script_dir, r"images\Start.jpg")
midimg = os.path.join(script_dir, r"images\mid_game.jpg")
himg = os.path.join(script_dir, r"images\snake-head.png")
fimg = os.path.join(script_dir, r"images\laddu.png")

stimg=pygame.image.load(stimg)
stimg=pygame.transform.scale(stimg,(screen_width,screen_height)).convert_alpha()
midimg=pygame.image.load(midimg)
midimg=pygame.transform.scale(midimg,(screen_width,screen_height)).convert_alpha()
himg=pygame.image.load(himg)
himg=pygame.transform.scale(himg,(25,25)).convert_alpha()
fimg=pygame.image.load(fimg)
fimg=pygame.transform.scale(fimg,(25,25)).convert_alpha()
# colors
black= (0,0,0)
red = (255,255,0)
green = (0,255,0)
blue = (0,0,255)
white= (255,255,255)

clock = pygame.time.Clock()
font1= pygame.font.SysFont('Harrington', 50)
font3= pygame.font.SysFont('Harrington', 70)
font2= pygame.font.SysFont('Harrington', 90)

# heigh Score
try:
    with open("high_scroe.txt","r") as f:
        heigh_scroe= int(f.read())
except:
    heigh_scroe=0
    with open("high_scroe.txt","w") as f:
        f.write(str(0))

# display text 
def show_text(text,color,text_x,text_y,font):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[text_x,text_y])

# display snake or its body

def show_snake(gamewindow,color,snake_body,snake_size):
    for x,y in snake_body:
        if x == snake_body[-1][0] and y == snake_body[-1][1]:
            gamewindow.blit(himg,(x,y))
        else:
            color = blue
            pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size]) 

# welcome Screen
def welcome_Screen():
    exit_game=False
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:           
                exit_game=True
            if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN:
                        file_name = r"music\abcd.mp3"
                        music_file = os.path.join(script_dir, file_name)
                        pygame.mixer.music.load(music_file)
                        pygame.mixer.music.play()
                        gameloop()

        gamewindow.fill(white)
        gamewindow.blit(stimg,(0,0))
        show_text(f"High Score : {heigh_scroe}",white,212,302,font3)
        show_text(f"High Score : {heigh_scroe}",green,210,300,font3)
        pygame.display.update()
        clock.tick(30)
    
# game loop
def gameloop():

    # game specific variables
    game_over=False
    exit_game=False
    snake_x = 45
    snake_y = 45
    snake_size=25
    init_velocity=15
    velocity_x=0
    velocity_y=0
    score=0
    food_x=random.randint(50,screen_width-50)
    food_y=random.randint(50,screen_height-90)
    fps = 10

    # snake increment
    snake_body =[]
    snake_lenght=1

    while not exit_game:
        if game_over:
            show_text("Game Over !",red,281,62,font3)
            show_text("Game Over !",white,280,60,font3)
            show_text(f"Your Score : {score}",black,150,150,font2)
            show_text("Press Enter to Restart",red,181,292,font1)
            show_text("Press Enter to Restart",white,180,290,font1)

            # Updating high score
            if heigh_scroe < score:
                with open("high_scroe.txt","w") as f:
                    f.write(str(score))
                show_text(f"High Score : {score}",white,152,352,font3)
                show_text(f"High Score : {score}",green,150,350,font3)

            # to exit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():

                # to exit the game
                if event.type == pygame.QUIT:
                    exit_game = True

                # to change the direction
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if velocity_x==0:
                            velocity_x = init_velocity
                            velocity_y = 0
                    elif event.key == pygame.K_LEFT:
                        if velocity_x==0:
                            velocity_x = -init_velocity
                            velocity_y = 0
                    elif event.key == pygame.K_UP:
                        if velocity_y == 0:
                            velocity_y = -init_velocity
                            velocity_x = 0
                    elif event.key == pygame.K_DOWN:
                        if velocity_y == 0:
                            velocity_y = init_velocity
                            velocity_x = 0

            # checking game over on walls
            if snake_x>screen_width-15 or snake_x<0 or snake_y<0 or snake_y>screen_height-88:
                game_over=True
                velocity_x=0
                velocity_y=0

            # movement of snake
            snake_x+=velocity_x
            snake_y+=velocity_y

            # change food locatain and score
            if abs(food_x-snake_x)<snake_size+1 and abs(food_y-snake_y)<snake_size+1:
                score+=10
                snake_lenght+=2
                while True:
                    food_x=random.randint(20,screen_width-50)
                    food_y=random.randint(20,screen_height-90)
                    if [food_x,food_y] in snake_body[:]:
                        print("yes it happens")
                    else:
                        break

            # for create snake
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snake_body.append(head)

            # mantain the length of snake
            if len(snake_body)>snake_lenght:
                del snake_body[0]

            # checking game over on body
            if head in snake_body[:-1]:
                game_over=True

            # set the screen and score
            gamewindow.fill(white)
            gamewindow.blit(midimg,(0,0))
            pygame.draw.rect(gamewindow,white,[0,screen_height-65,screen_width,10])
            show_text(f"Score : {score}",white,30,(screen_height-60),font1)
            show_snake(gamewindow,blue,snake_body,snake_size)
            gamewindow.blit(fimg,(food_x,food_y))

        # updating the screen
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome_Screen()

# ------- code to pass the game over on wall
# if snake_x>screen_width-10:
#     snake_x= 0
# elif snake_x<0:
#     snake_x=screen_width-10
# if snake_y<0:
#     snake_y=screen_height-10
# elif snake_y>screen_height-10:
#     snake_y=0        