#! /usr/bin/python
#insert pygame library
import pygame
from pygame import *
#Camera Size for game
WIN_WIDTH = 256 * 3
WIN_HEIGHT = 224 * 3
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0

# Zuchi Character Frame work Inside Game

spritesheet = pygame.image.load("Media/Zuchi.png")

character = Surface((31,45),pygame.SRCALPHA)
character.blit(spritesheet,(0,-9))
character = pygame.transform.scale(character, (25*2,45*3))
ZuchiStand = character

character = Surface((31,45),pygame.SRCALPHA)
character.blit(spritesheet,(-81,-9))
character = pygame.transform.scale(character, (25*2,45*3))
ZuchiRun = character

character = Surface((27,45),pygame.SRCALPHA)
character.blit(spritesheet,(-118,-120))
character = pygame.transform.scale(character, (31*2,45*3))
Zuchileft = character

character = Surface((31,38),pygame.SRCALPHA)
character.blit(spritesheet,(-406,-124))
character = pygame.transform.scale(character, (31*2,38*3))
ZuchiJump = character


# Goomba Frame work for Game

spritesheet = pygame.image.load("Media/smb.png")

character = Surface((16, 16), pygame.SRCALPHA)
character.blit(spritesheet, (0, -4))
character = pygame.transform.scale(character, (25 * 3, 16 * 3))
goombawalk1 = character

character = Surface((16, 16), pygame.SRCALPHA)
character.blit(spritesheet, (-30, -4))
character = pygame.transform.scale(character, (25 * 3, 16 * 3))
goombawalk2 = character

character = Surface((16, 16), pygame.SRCALPHA)
character.blit(spritesheet, (-60, 0))
character = pygame.transform.scale(character, (16 * 2, 16 * 3))
goombaflat1 = character


character = Surface((16, 16), pygame.SRCALPHA)
character.blit(spritesheet, (-60, 0))
character = pygame.transform.scale(character, (100 * 2, 16 * 3))
goombaflat1 = character

#Main Class for Initializing
def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()

    up = down = left = right = running = False

    bg = Surface((WIN_WIDTH, WIN_HEIGHT)).convert()
    entities = pygame.sprite.Group()
    enemygroup = pygame.sprite.Group()
    player = Player(16 * 3, 16 * 3 * 22)

    enemygroup.add(Goomba(16 * 3 * 6, 16 * 3 * 2))
    enemygroup.add(Goomba(16 * 3 * 6, 16 * 3 * 2))
    enemygroup.add(Goomba(16 * 3 * 6, 16 * 3 * 2))
    enemygroup.add(Goomba(16 * 3 * 6, 16 * 3 * 2))
    enemygroup.add(Goomba(16 * 2* 6, 16 * 3 * 2))
    enemygroup.add(Goomba(16 * 3 * 6, 16 * 3 * 2))
    enemygroup.add(Goomba(16 * 3 * 6, 16 * 3 * 2))
    enemygroup.add(Goomba(16 * 3 * 9, 16 * 3 * 2))
    enemygroup.add(Goomba(16 * 3 * 12, 16 * 3 * 23))
    enemygroup.add(Goomba(16 * 3 * 12, 16 * 3 * 23))
    enemygroup.add(Goomba(16 * 3 * 12, 16 * 3 * 15))
    enemygroup.add(Goomba(16 * 3 * 12, 16 * 3 * 23))

    platforms = []

    x = y = 0
    level = [
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
        "P                                          P",
        "P                                          P",
        "P                                          P",
        "P                    PPPPPPPPPPP           P",
        "P                  PP                      P",
        "P                PP                        P",
        "P                                          P",
        "P    PPPPPPPP                              P",
        "P            PP                            P",
        "P                          PPPPPPP         P",
        "P                 PPPPPP                   P",
        "P                                          P",
        "P         PPPPPPP                          P",
        "P       PP                                 P",
        "P                     PPPPPP               P",
        "P                                          P",
        "P   PPPPPPPPPPP                            P",
        "P                                          P",
        "P                 PPPPPPPPPPP              P",
        "P                            PP            P",
        "P                              PP          P",
        "P                                          P",
        "P                                          P",
        "PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP", ]
    # build the level
    for row in level:
        for col in row:
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            x += 16 * 3
        y += 16 * 3
        x = 0

    total_level_width = len(level[0]) * 16 * 3
    total_level_height = len(level) * 16 * 3
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

        screen.blit(bg, (0, 0))

        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, running, platforms, enemygroup)

        for e in entities:
            screen.blit(e.image, camera.apply(e))
        for e in enemygroup:
            screen.blit(e.image, camera.apply(e))
            e.update(platforms, entities)

        pygame.display.update()


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)


def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l + HALF_WIDTH, -t + HALF_HEIGHT, w, h

    l = min(0, l)  # stop scrolling at the left edge
    l = max(-(camera.width - WIN_WIDTH), l)  # stop scrolling at the right edge
    t = max(-(camera.height - WIN_HEIGHT), t)  # stop scrolling at the bottom
    t = min(0, t)  # stop scrolling at the top
    return Rect(l, t, w, h)


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.faceright = True
        self.onGround = False
        self.airborne = False
        self.counter = 0
        self.image = ZuchiStand
        self.rect = Rect(x, y, 16 * 3, 32 * 3)

    def update(self, up, down, left, right, running, platforms, enemygroup):

        if up:
            # only jump if on the ground
            if self.onGround: self.yvel -= 10
        if down:
            pass
        if running:
            self.xvel = 12
        if left:
            self.xvel = -8
            self.faceright = False
        if right:
            self.xvel = 8
            self.faceright = True
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not (left or right):
            self.xvel = 0
        if self.yvel < 0 or self.yvel > 1.2: self.airborne = True
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms, enemygroup)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms, enemygroup)

        self.animate()

    def collide(self, xvel, yvel, platforms, enemygroup):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.airborne = False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        for e in enemygroup:
            if pygame.sprite.collide_rect(self, e):
                dif = self.rect.bottom - e.rect.top
                if dif <= 8:
                    self.yvel = - 8
                else:
                    pygame.event.post(pygame.event.Event(QUIT))

    def animate(self):

        if self.xvel > 0 or self.xvel < 0:
            self.walkloop()
            if self.airborne: self.updatecharacter(ZuchiJump)
        else:
            self.updatecharacter(ZuchiStand)
            if self.airborne: self.updatecharacter(ZuchiJump)

    def walkloop(self):
        if self.counter == 5:
            self.updatecharacter(ZuchiRun)
        elif self.counter == 10:
            self.updatecharacter(ZuchiRun)
        elif self.counter == 15:
            self.updatecharacter(ZuchiRun)
            self.counter = 0
        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        if not self.faceright: ansurf = pygame.transform.flip(ansurf, True, False)
        self.image = ansurf


class Goomba(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = -3
        self.yvel = -2
        self.onGround = False
        self.destroyed = False
        self.counter = 0
        self.image = goombawalk1
        self.rect = Rect(x, y, 16 * 3, 16 * 3)

    def update(self, platforms, entities):
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 10
            # max falling speed
            if self.yvel > 100: self.yvel = 100

        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms, entities)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms, entities)

        self.animate()

    def collide(self, xvel, yvel, platforms, entities):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.xvel = -abs(xvel)
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    self.xvel = abs(xvel)
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        for p in entities:
            if pygame.sprite.collide_rect(self, p):
                dif = p.rect.bottom - self.rect.top
                if dif <= 8:
                    self.destroyed = True
                    self.counter = 0
                    self.xvel = 0

    def animate(self):

        if not self.destroyed:
            self.walkloop()
        else:
            self.destroyloop()

    def walkloop(self):
        if self.counter == 10:
            self.updatecharacter(goombawalk1)
        elif self.counter == 20:
            self.updatecharacter(goombawalk2)
            self.counter = 0
        self.counter = self.counter + 1

    def destroyloop(self):
        if self.counter == 0:
            self.updatecharacter(goombaflat1)
        elif self.counter == 10:
            self.kill()
        self.counter = self.counter + 1

    def updatecharacter(self, ansurf):
        self.image = ansurf


class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = pygame.image.load("Media/faithful.png").convert()
        self.image = pygame.transform.scale(self.image, (16 * 3, 16 * 3))
        self.rect = Rect(x, y, 16 * 3, 16 * 3)

    def update(self):
        pass


class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))


if __name__ == "__main__":
    main()