from Asteroid import Asteroid,Base_stats
from Player import Spaceship,Bullet

import pygame
import math
import random
import sys

pygame.init()
font = pygame.font.SysFont("Garamond MS",20)
clock = pygame.time.Clock()

# Asteroid layers, speed=0, linear=0, amount
levelData = {
    1:  [2, 0, 1, 3],
    2:  [2, 0, 1, 5],
    3:  [2, 2, 1, 7],
    4:  [2, 2, 0, 9],
    
    5:  [3, 0, 1, 3],
    6:  [3, 0, 1, 4],
    7:  [3, 0, 1, 5],
    8:  [3, 2, 1, 6],
    9:  [3, 2, 1, 7],
    10: [3, 2, 0, 8],
    
    11: [4, 0, 1, 3],
    12: [4, 0, 1, 3],
    13: [4, 2, 1, 4],
    14: [4, 2, 1, 4],
    15: [4, 2, 1, 5],
    16: [4, 3, 1, 5],
    17: [4, 3, 1, 5],
    18: [4, 3, 0, 6],

    19: [5, 0, 1, 2],
    20: [5, 0, 1, 2],
    21: [5, 0, 1, 2],
    22: [5, 2, 1, 3],
    23: [5, 2, 1, 3],
    24: [5, 2, 1, 3],
    25: [5, 2, 1, 4],
    26: [5, 2, 1, 4],
    27: [5, 3, 1, 4],
    28: [5, 3, 0, 3],
    
    29: [6, 0, 1, 1],
    30: [6, 0, 1, 1],
    31: [6, 0, 1, 1],
    32: [6, 2, 1, 2],
    33: [6, 2, 1, 2],
    34: [6, 2, 1, 2],
    35: [6, 3, 1, 1],
    36: [6, 3, 1, 2],
    37: [6, 3, 1, 3],
    38: [6, 3, 1, 4],
    39: [6, 4, 1, 3],
    40: [6, 4, 1, 2],

    41: [7, 0, 0, 1],
    42: [8, 0, 0, 1],
    43: [9, 0, 0, 1],
    44: [10,0, 0, 1],

    45: [7, 2, 0, 2],
    46: [8, 2, 0, 2],
    47: [9, 2, 0, 2],
    48: [10,2, 0, 2],
         
    49: [10,4, 0, 2],
    50: [10,2, 0, 3]
}

__LEVEL_COUNT__ = len(levelData.keys())
__BOSS_LEVELS__ = [4,10,18,28,40,44,45,46,47,48,49]
__FINAL_LEVEL__ = 50
    
class Levelmaster:
    def __init__(self,surf,level):
        self.surf = surf
        self.lives = 5
        self.level = level+1

    def get_rocks(self):
        # any, 1.5, True
        stage,speed,linear,amount = levelData[self.level]

        Base_stats.base_stage = stage
        Base_stats._speed = speed if speed else Base_stats._speed
        Base_stats.linear_divide = linear

        return [Asteroid(self.surf) for _ in range(amount)]
        
    def run(self):
        ship = Spaceship(self.surf)
        lvl = font.render(f"Level {self.level}",True,(0,255,0))

        rocks = self.get_rocks()

        while True:
            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        ship.shoot()

                    elif event.key == pygame.K_e:
                        ship.shoot()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        ship.shoot()

            if pygame.key.get_pressed()[pygame.K_UP]:
                ship.shove()
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                ship.rotate_left()
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                ship.rotate_right()

            self.surf.fill((0,0,0))
            ship.draw()
            ship.move()

            rocks = ship.break_rocks(rocks)

            for i in rocks:
                i.draw()
                i.move()

            for i in range(self.lives):
                pygame.draw.circle(self.surf,(200,40,20),[20+(i*15),40],6,1)
            self.surf.blit(lvl,lvl.get_rect(topleft=[20,20-(0.5*lvl.get_height())]))

            pygame.display.flip()

            if ship.collide(rocks):
                self.lives -= 1

                for iteration in range(50):
                    if ship.collide(rocks):
                        ship.reposition()
                    else:
                        break
                else:
                    if not ship.reposition(True,rocks):
                        self.lives = 0
                    
            if not self.lives or not len(rocks):
                return {"Lives":self.lives,"Level":self.level}
