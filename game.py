import pygame
import random
from os import path
img_dir=path.join(path.dirname(__file__),'img')
width=480
height=600
fps=60
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue= (0,0,255)
yellow = (255,255,0)
'''pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Shooting Game")
clock=pygame.time.Clock()
font_name=pygame.font.match_font('arial')''' #finds the closest match rather than exact match
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text , True, white)#true is set for anti alias
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #built in sprite without which sprite will not work
        self.image = pygame.transform.scale(player_img,(115,150))#mandatory in Sprite
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()#mandatory in Sprite
        self.radius = 45
        #pygame.draw.circle(self.image,red,self.rect.center self.radius)
        self.rect.centerx = width//2 #center of the width positining of the player ret
        self.rect.bottom = height #10 pixel above bottom
        self.speedx = 0 #controls how fast in pixel the player should move..start at zero
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self): #things that will happen everytime the animation happnes
        self.speedx = 0 #sholdnot be moving
        keystate = pygame.key.get_pressed() #gives the list of keys that are pressed
        if(keystate[pygame.K_LEFT]):
            self.speedx = -8 #increase the value to -8 or 8 to move faster
        if (keystate[pygame.K_RIGHT]):
            self.speedx = 8
        if (keystate[pygame.K_SPACE]):
            self.shoot()
        self.rect.x += self.speedx #move at the given sp  eedx
        if self.rect.right > width:
            self.rect.right=width
        if self.rect.left < 0:
            self.rect.left=0
    def shoot(self):
        now = pygame.time.get_ticks()
        if (now - self.last_shot) > self.shoot_delay:
            self.last_shot = now
            bullet=Bullet(self.rect.centerx,self.rect.top)
            all_sprites.add(bullet)
            bullets.add(bullet)
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(mob_images)#mandatory in Sprite
        self.image_orig.set_colorkey(black)
        self.image = self.image_orig.copy()
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width *.75 /2)
        #pygame.draw.circle(self.image,red,self.rect.center,self.radius)
        self.rect.x=random.randrange(width)
        self.rect.y = random.randrange(-150,-100)
        self.speedy=random.randrange(1,8)
        self.speedx=random.randrange(-3,3)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()
    def rotate(self):
        now = pygame.time.get_ticks()
        if (now - self.last_update > 50):
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig,self.rot)
            old_center = self.rect.center
            self.image=new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y +=self.speedy
        if(self.rect.right>=width):
            self.speedx = - self.speedx
        if(self.rect.left<=0):
            self.speedx = -self.speedx
        if (self.rect.top > height + 10)  or (self.rect.left < -25) or (self.rect.right > width + 20):
            self.rect.x=random.randrange(width - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy=random.randrange(1,8)
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bullet_img,(30,30))#mandatory in Sprite
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.radius=15
        #pygame.draw.circle(self.image,red,self.rect.center,self.radius)
        self.rect.bottom = y
        self.rect.centerx = x-20
        self.speedy= -10
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explo_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50#for faster explosion make small
    def update(self):
        now = pygame.time.get_ticks()
        if (now - self.last_update > self.frame_rate):
            self.last_update = now #last update will get updated
            self.frame +=1#add one to frame_rate
            if self.frame == len(explo_anim[self.size]):
                self.kill()#kill when get to end one
            else:
                center = self.rect.center
                self.image = explo_anim[self.size][self.frame] #changing the image of explosion
                self.rect = self.image.get_rect()
                self.rect.center = center
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Shooting Game")
clock=pygame.time.Clock()
font_name=pygame.font.match_font('arial')
def show_go_screen():
    screen.blit(background,background_rect)
    draw_text(screen,"GAME!",64,width//2,height//4)
    draw_text(screen,"Arrow keys to move, Space to fire",32,width//2,height//2)
    draw_text(screen,"Press any key to begin",24,width//2,(height*3)//4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get(): #checking the events
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
background = pygame.image.load(path.join(img_dir,"bg4.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir,"naru.png")).convert()
#mob_img = pygame.image.load(path.join(img_dir,"shuri.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir,"rasen.png")).convert()
mob_images=[]
mob_list=['shuri1.png','shuri.png','shuri2.png','shuri3.png','shuri4.png','shuri4.png','shuri6.png']
for img in mob_list:
    mob_images.append(pygame.image.load(path.join(img_dir,img)).convert())
explo_anim = {} #dictonary
explo_anim['lg']=[]
explo_anim['sm']=[]
for i in range(6):
    filename='expo0{}.png'.format(i) #the bracket will be filled with whatever is in the format
    img = pygame.image.load(path.join(img_dir,filename)).convert()
    img.set_colorkey(black)
    #img_lg = pygame.transform.scale(img,(75,75))
    explo_anim['lg'].append(img)

#game loop

game_over = True
running= True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites=pygame.sprite.Group()
        mobs = pygame.sprite.Group() #create the group of mobs
        bullets = pygame.sprite.Group()
        player = Player() #creating object of class palyer
        all_sprites.add(player) #adding the player in the sprite group for display
        for i in range(8):
            m=Mob()
            all_sprites.add(m)
            mobs.add(m)
        score=0
    clock.tick(fps)
    #Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    all_sprites.update()
    #check to see if the bullet hits the mobs
    hits = pygame.sprite.groupcollide(mobs,bullets,True,True,pygame.sprite.collide_circle)#1st true for deleting mobs and 2nd true for deleting bullets
    for hit in hits:
        score += 50 - hit.radius
        m = Mob()
        all_sprites.add(m)
        expl = Explosion(hit.rect.center,'lg')
        all_sprites.add(expl)
        mobs.add(m)
    #check to see if the mob hit the Player
    hits = pygame.sprite.spritecollide(player,mobs,False,pygame.sprite.collide_circle) #gives a list of any of the mobs that hit the player..should be deleted-False
    if hits:
        game_over = True
    screen.fill(black)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 24, width/2, 10)
    pygame.display.flip()
pygame.quit()
