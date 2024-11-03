import math,random,pygame
sw,sh=800,500
psx,psy=370,380
esx,esy=2,20
bullet_y=10
collion=27
game_over_threshold=psy-40
pygame.init()
screen=pygame.display.set_mode((sw,sh))
pygame.display.set_caption("space invader")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
background=pygame.image.load("background.png")
playerimage=pygame.image.load("player.png")
enemy_image=pygame.image.load("enemay.png")
bullet_image=pygame.image.load("bullet.png")
font=pygame.font.Font("freesansbold.ttf",32)
over_font=pygame.font.Font("freesansbold.ttf",64)
playerx,playery,playerx_change=psx,psy,0
enemies=[{
    "x":random.randint(0,sw-64),
    "y":random.randint(50,150),
    "dx":esx
}for _ in range(6)]
score=0
bulletX, bulletY, bullet_state = 0, psy, "ready"
def show_score():
    screen.blit(font.render("score"+str(score),True,(255,255,255)),(10,10))
def show_gameover():
    screen.blit(font.render("gameover",True,(255,255,255)),(200,250))    
def draw_player():
    screen.bilt(playerimage,(playerx,playery))   
def draw_enemy(enemy):
    screen.blit(enemy_image,(enemy["x"],enemy["y"]))    
def fire_bullet():
    screen.blit(bullet_image,[bulletX+16,bulletY+10])    