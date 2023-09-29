import pygame as pg


pg.init()

screen_width = 800
screen_height=600


display =pg.display.set_mode((screen_width,screen_height))
#pg.display.set_caption('')
#icon_ima == pg_image.load('')

background_img = pg.image.load('resources/img/background.png')
display.blit(background_img,(0,0))
#sysfont=pg.front.SysFont('arial',40)
sysfont=pg.font.SysFont('arial',60)
text_img = sysfont.render('Minn Latt', True, 'white')
w =text_img.get_width()
h =text_img.get_height()
x =screen_width-w
#display.blit(text_img,(x,0))

#player
player_img = pg .image.load('resources/img/player.png')
player_width=player_img.get_width()
player_height=player_img.get_height()
player_x=screen_width/2.player_width/2
player_y=screen_height_player_height
player_velocity=1
player_dx=0

#pyla
bullet_img = pg .image.load('resources/img/bullet.png')
player_width=player_img.get_width()
player_height=player_img.get_height()
player_x=screen_width/2.player_width/2
player_y=screen_height_player_height
player_velocity=1
player_dx=0

running = True


while running:

    #display.fill('blue',(30,50,100,250))
    display.blit(text_img,(x,0))
    pg.display.update()



    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN and event.key ==pg.K_q:
            running = False
        if event.type==pg.KEYDOWN and event.key ==

pg.quit()
