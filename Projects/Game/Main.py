#Modules
import pygame
from sys import exit
from random import randint
from pygame import mixer

#Initialising the game:
pygame.init() #Used to start the sub-part of the pygame
mixer.init()

#Background Music:
pygame.mixer.music.load("C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\audio\\music2.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

#Functions:
def display_score():
    current_time = int(pygame.time.get_ticks() /1000) - start_time #int to avoid flotting nos.
    score_surface = score_font.render(f'Score: {current_time}', False,(64,64,64))
    score_rect = score_surface.get_rect(center =(400,50))
    screen.blit(score_surface,score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom ==300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

                obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list

    else:
        return[]
def collisions(player,obstacle):
    if obstacle:
        for obstacle_rect in obstacle:
            if player.colliderect(obstacle_rect):
                pygame.mixer.music.pause()
                death_sound = pygame.mixer.Sound("C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\audio\\death.mp3") 
                death_sound.set_volume(0.5)
                pygame.mixer.Sound.play(death_sound)
                return False

    return True
def player_animation():
    global player_surf, player_index

    if player_rect.bottom <300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

#Variables
screen = pygame.display.set_mode((800,400)) #(width,height) #only has one frame right at this moment
pygame.display.set_caption('Pixel Runner')
logo = pygame.image.load("C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\Player\\jump.png")
pygame.display.set_icon(logo)
clock = pygame.time.Clock() #Setting the frame rate
score_font= pygame.font.Font('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\font\\Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

#Static Surfaces
sky_surface = pygame.image.load('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\Sky.png').convert_alpha() #Surface 1
ground_surface = pygame.image.load('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\ground.png').convert_alpha() #Surface 2

#Obstacles
snail_frame_1 = pygame.image.load('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\snail\\snail1.png').convert_alpha()
snail_frame_2= pygame.image.load('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\snail\\snail2.png').convert_alpha()
snail_frames = [snail_frame_1,snail_frame_2]
snail_frame_index = 0
snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load("C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\Fly\\fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\Fly\\fly2.png").convert_alpha()
fly_frames = [fly_frame_1,fly_frame_2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list =[]

#Player Surface
player_walk_1 = pygame.image.load('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\Player\\player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\Player\\player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0 
player_jump = pygame.image.load('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\Player\\jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#Intro Screen elements:
player_stand = pygame.image.load('C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\graphics\\Player\\player_stand.png').convert_alpha()
player_stand= pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = score_font.render(('Pixel Runner'),False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,70))

game_message = score_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,335))


#Timer:
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT +2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT +3
pygame.time.set_timer(fly_animation_timer,200)

#Game Loop:
while True:
    #To EXIT the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #To break the while loop


        if game_active:
            #To START and PLAY the game with SPACEBAR + Jump sound
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                    sound = pygame.mixer.Sound("C:\\Users\\india\\Desktop\\Python\\Projects\\Game\\audio\\jump.mp3") 
                    sound.set_volume(0.1)
                    pygame.mixer.Sound.play(sound)

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() /1000)
                pygame.mixer.music.unpause()

        if game_active: #Spawn the enemies i.e Snail + Fly
            if event.type == obstacle_timer:
                if randint(0,2): obstacle_rect_list.append(snail_surface.get_rect(midbottom =(randint(900,1100),300)))
                else: obstacle_rect_list.append(snail_surface.get_rect(midbottom =(randint(900,1100),210)))

            if event.type == snail_animation_timer: 
                if snail_frame_index ==0: snail_frame_index =1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index =1
                else: fly_frame_index =0 
                fly_surface = fly_frames[fly_frame_index]
            

    if game_active: #Adding the elements on the screen
        screen.blit(sky_surface,(0,0)) #to put one surface on another #Use a modified cratisiian plane (origion at the top left corner)
        screen.blit(ground_surface,(0,300))
        score = display_score()

        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        
        player_animation()
        screen.blit(player_surf,player_rect)

        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Collisions:
        game_active = collisions(player_rect,obstacle_rect_list)
    
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        score_message = score_font.render(f'Your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400, 335))
        screen.blit(game_name,game_name_rect)

        #Outro Screen 
        if score == 0: screen.blit(game_message,game_message_rect)
        else: screen.blit(score_message, score_message_rect)

    pygame.display.update() #Updates the screen for the player
    clock.tick(60) #fps (Frames per second)