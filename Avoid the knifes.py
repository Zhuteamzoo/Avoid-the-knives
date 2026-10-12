#Avoid the knives made by Terence Zhu on octobre 13th 2025 
#enjoy the game :)

import pygame
import random
import time
import button

random.random
pygame.init()
pygame.font.init()
pygame.display.set_caption("Avoid the knives")
#Main setup
W, H = 500,700
screen =pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
running = True
#uhh random ahh variable
dt=0
started = False
elapsed_time = 0
hit = False
#player variables
player_pos = pygame.Vector2(screen.get_width()/2,H)
player_size = 50
player = pygame.image.load('geometry_dash_cube_by_maximusreed_dghe626-fullview.png')
player = pygame.transform.scale(player, (player_size,player_size))

#Font variables
FONT = pygame.font.SysFont("comicsans", 30)
FONT_2=pygame.font.SysFont("comicsans",20)
FONT_3 = pygame.font.SysFont("impact",50)
#knife variables
knife_size = 30
knife = pygame.image.load('knife.png')
knife = pygame.transform.scale(knife, (knife_size,knife_size))
knifes = []
amount_knifes = 0
knifes_add_increment = 2000
knife_add = 5
knife_vel = 3
#button variables
start_img = pygame.image.load("tl.webp").convert_alpha()
start_img = pygame.transform.scale(start_img,(200,75))
exit_img = pygame.image.load("R.png").convert_alpha()
exit_img = pygame.transform.scale(exit_img, (200,75))

def game(dt,running,screen,clock,hit,W,H,player_pos,player_size,player,FONT,FONT_2,knife_size,knife,knifes,amount_knifes,knifes_add_increment,knife_add,knife_vel):
#game loop
    start_time = time.time()
    while running:
#random ahhh variable
        ms = clock.tick(60)
        dt = ms/1000
        amount_knifes += ms
        #time variables
        elapsed_time = time.time()-start_time
#rectangle/hitbnoxes
        rect_player = pygame.Rect(player_pos.x+6,H-player_size+6,player_size-12,player_size-12)
#knife generation
        if amount_knifes > knifes_add_increment:
            for _ in range(knife_add):
                knife_x = random.randint(0,W-knife_size)
                rect_knife = pygame.Rect(knife_x,-knife_size,knife_size,knife_size)
                knifes.append((rect_knife,knife))
#how fast knife drop       
            knifes_add_increment = max(200, knifes_add_increment-50)
            amount_knifes = 0
#loop             
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
#draw
        def draw(screen, elapsed_time,knifes,knife):
            screen.fill("white")
            screen.blit(player,(player_pos.x,H-player_size))
            for rect_knife,knife in knifes:
                screen.blit(knife, rect_knife.topleft)
            time_text = FONT.render(f"Time:{round(elapsed_time)}s",1,("black"))
            screen.blit(time_text,(10,10))
            pygame.display.update()
#move the charachter
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player_pos.x > -5:
            player_pos.x -= 600*dt
        if keys[pygame.K_d] and player_pos.x <W-45:
            player_pos.x += 600*dt
#hit
        for rect_knife,knife in knifes[:]:
            rect_knife.y += knife_vel
            if rect_knife.y >H:
                knifes.remove((rect_knife,knife))
            elif rect_knife.colliderect(rect_player):
                knifes.remove((rect_knife,knife))
                hit = True
                break

#functions
        draw(screen, elapsed_time,knifes,knife)
#death
        if hit == True:
            lost_text = FONT_2.render(f'You lost.Your time was:{round(elapsed_time)}s',1,"Black")
            screen.blit(lost_text,(W/2-lost_text.get_width()/2,H/2-lost_text.get_width()/2))
            pygame.display.update()
            pygame.time.delay(3000)
            knifes.clear()
            amount_knifes = 0
            knifes_add_increment = 2000
            player_pos = pygame.Vector2(screen.get_width()/2,H)
            running = False
            break

    pygame.QUIT
def main_menu(running):
    start_button = button.Button(W/2-100,200,start_img)
    exit_button = button.Button(W/2-100,400,exit_img)

    while running:

        screen.fill((202,228,241))
        Title = FONT_3.render("AVOID THE KNIVES",1,"black")
        screen.blit(Title,(75,30))
        Name = FONT_2.render("Made by Terence Zhu",1,"black")
        screen.blit(Name,(150,80))
        if start_button.draw(screen) == True:
            print('Start')
            game(dt,running,screen,clock,hit,W,H,player_pos,player_size,player,FONT,FONT_2,knife_size,knife,knifes,amount_knifes,knifes_add_increment,knife_add,knife_vel)
        if exit_button.draw(screen) == True:
            print('Exit')
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        pygame.display.update()

    pygame.QUIT
                

main_menu(running)