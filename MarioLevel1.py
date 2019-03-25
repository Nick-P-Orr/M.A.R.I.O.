import pygame
import numpy
import time
from math import floor
from copy import deepcopy

class MarioLevel:
    size = None
    height, width = None, None
    screen = None
    blocks = []
    visual = [0]
    block_rects = []
    mario_loc = []
    done = None
    run_once = None
    keypress = []
    offset = 0
    show = True
    dead = False

    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 512,256
        if self.show:
            self.screen = pygame.display.set_mode((self.size))
        #0 is nothing, 1 is blocks
        self.blocks = [
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,2,0,0,0,0,0,1,1,0,0,0,2,0,2,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,0,2,0,2,0,2,0,2,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,2,0,2,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                      ]
        self.enemies = []
        for i, y in enumerate(self.blocks):
            for n, x in enumerate(y):
                if x == 2:
                    self.enemies.append([n*16, i*16, 0])

        self.visual = self.getVisual(0)
                            
        #                 y,  x, xs, ys, grounded, jump start speed
        self.mario_loc = [176,120, 0, 0, True, 0]
        done = False
        run_once = False

    def getVisual(self, off):
        if off < 0:
            off = 0
        vis = deepcopy(self.blocks)
        for i in range(len(vis)):
            vis[i] = vis[i][off:off+16]
        return vis

    def marioBlock(self):
        return floor(self.mario_loc[1]/16)-7

    def acceptInput(self, commands):
        if commands == None:
            return [0,self.visual]

        self.keypress = commands
        self.handlePhysics()
        if self.mario_loc[0] > 190 or self.dead:
            return [self.mario_loc[1], self.visual, True] 
        return [self.mario_loc[1], self.visual, False]

    def acceptInputHuman(self):
        while 1:
            self.keypress = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.keypress.append(0)
                    if event.key == pygame.K_RIGHT:
                        self.keypress.append(1)
                    if event.key == pygame.K_LCTRL:
                        self.keypress.append(2)
                    if event.key == pygame.K_SPACE:
                        self.keypress.append(3)
                    self.handlePhysics()

    def handlePhysics(self):
        min_speed = 1.1875
        walk_accel = 0.59375
        run_accel = 0.890625
        release_decel = -0.8125
        skid_decel = -1.625
        max_run_speed = 41/16
        skid_turnaround_speed = 9

        jump_speed = [-4, -4, -5]
        jumping_gravity = [2/16, 1.875/16, 2.5/16]
        falling_gravity = [7/16, 6/16, 9/16]

        air_forward_speed = [0.59375/256, 0.890625/256]
        air_backward_speed = [-0.890625/256, -0.8125/256, -0.59375/256]

        mario_rect = pygame.Rect(120,self.mario_loc[0],16,16)

        if self.mario_loc[4]:
            if 1 in self.keypress and not 0 in self.keypress and self.mario_loc[2] < max_run_speed:
                if self.mario_loc[2] < 0 and self.mario_loc[2] > skid_turnaround_speed * -1:
                    self.mario_loc[2] *= -1
                elif self.mario_loc[2] < 0:
                        self.mario_loc[2] -= skid_decel
                elif self.mario_loc[2] == 0:
                    self.mario_loc[2] = min_speed
                elif 2 in self.keypress:
                    self.mario_loc[2] += run_accel
                else:
                    self.mario_loc[2] += walk_accel
            elif 0 in self.keypress and not 1 in self.keypress and self.mario_loc[2] > max_run_speed * -1:
                if self.mario_loc[2] > 0 and self.mario_loc[2] < skid_turnaround_speed:
                    self.mario_loc[2] *= -1
                elif self.mario_loc[2] > 0:
                        self.mario_loc[2] += skid_decel
                elif self.mario_loc[2] == 0:
                    self.mario_loc[2] = min_speed * -1
                elif 2 in self.keypress:
                    self.mario_loc[2] -= run_accel
                else:
                    self.mario_loc[2] -= walk_accel
            else:
                if self.mario_loc[2] > 0:
                    self.mario_loc[2] += release_decel
                elif self.mario_loc[2] < 0:
                    self.mario_loc[2] -= release_decel
        else:
            if 1 in self.keypress and not 0 in self.keypress and self.mario_loc[2] < max_run_speed:
                if self.mario_loc[2] >= 0:
                    if self.mario_loc[2] < 25:
                        self.mario_loc[2] += air_forward_speed[0]
                    else:
                        self.mario_loc[2] += air_forward_speed[1]
                else:
                    if self.mario_loc[2] >= 25:
                        self.mario_loc[2] += air_backward_speed[0]
                    elif self.mario_loc[2] < 25:
                        if self.mario_loc[5] >= 29:
                            self.mario_loc[2] += air_backward_speed[1]
                        else:
                            self.mario_loc[2] += air_backward_speed[2]

            if 0 in self.keypress and not 1 in self.keypress and self.mario_loc[2] > max_run_speed*-1:
                if self.mario_loc[2] <= 0:
                    if self.mario_loc[2] > -25:
                        self.mario_loc[2] -= air_forward_speed[0]
                    else:
                        self.mario_loc[2] -= air_forward_speed[1]
                else:
                    if self.mario_loc[2] <= -25:
                        self.mario_loc -= air_backward_speed[0]
                    elif self.mario_loc[2] > -25:
                        if self.mario_loc[5] <= -29:
                            self.mario_loc[2] -= air_backward_speed[1]
                        else:
                            self.mario_loc[2] -= air_backward_speed[2]
        if 3 in self.keypress:
            if self.mario_loc[2] > -16 and self.mario_loc[2] < 16:
                if self.mario_loc[4]:
                    self.mario_loc[3] = jump_speed[0]
                    self.mario_loc[5] = self.mario_loc[2]
                else:
                    self.mario_loc[3] += jumping_gravity[0]
            elif abs(self.mario_loc[2]) >= -16 and abs(self.mario_loc[2]) < 36.99609375:
                if self.mario_loc[4]:
                    self.mario_loc[3] = jump_speed[1]
                else:
                    self.mario_loc[3] += jumping_gravity[1]
            else:
                if self.mario_loc[4]:
                    self.mario_loc[3] = jump_speed[2]
                else:
                    self.mario_loc[3] += jumping_gravity[2]
        elif not self.mario_loc[4]:
            if self.mario_loc[2] > -16 and self.mario_loc[2] < 16:
                self.mario_loc[3] += falling_gravity[0]
            elif abs(self.mario_loc[2]) >= -16 and abs(self.mario_loc[2]) < 36.99609375:
                self.mario_loc[3] += falling_gravity[1]
            else:
                self.mario_loc[3] += falling_gravity[2]

        #self.mario_loc[1] += self.mario_loc[2]
        collide_h = False
        for rect in self.block_rects:
            if mario_rect.colliderect(pygame.Rect(rect.left-self.mario_loc[2], rect.top, rect.width+self.mario_loc[2], rect.height)):
                collide_h = True
                """if self.mario_loc[2] > 0:
                    self.mario_loc[1] = rect.left-16+self.offset
                    self.mario_loc[2] = 0
                else:
                    self.mario_loc[1] = rect.right+2+self.offset
                    self.mario_loc[2] = 0"""
        if not collide_h:
            self.mario_loc[1] += self.mario_loc[2]  
        
        #self.mario_loc[0] += self.mario_loc[3]
        flag = 0
        hit_rect = None
        for rect in self.block_rects:
            if self.mario_loc[3] < 0 and mario_rect.colliderect(pygame.Rect(rect.left, rect.top-self.mario_loc[3], rect.width, rect.height)):
                flag = 1
                hit_rect = rect
            elif self.mario_loc[3] > 0 and mario_rect.colliderect(pygame.Rect(rect.left, rect.top-self.mario_loc[3], rect.width, rect.height+self.mario_loc[3])):
                flag = 2
                hit_rect = rect
            elif mario_rect.colliderect(pygame.Rect(rect.left, rect.top-1, rect.width, rect.height+1)) and self.mario_loc[3] == 0:
                flag = 3
                hit_rect = rect

        if flag > 0:
            if flag == 1:
                self.mario_loc[3] *= -1
                self.mario_loc[0] += self.mario_loc[3]
            else:
                self.mario_loc[4] = True
        else:
            self.mario_loc[4] = False
            self.mario_loc[0] += self.mario_loc[3]

        self.visual = self.getVisual(self.marioBlock())

        self.moveEnemies()
        self.collideEnemies()

        self.updateScreen()

    def moveEnemies(self):
        n = 0
        enemy_speed = 1/2
        for enemy in self.enemies:
            if enemy[0] - self.mario_loc[1] <= 256 and enemy[0] - self.mario_loc[1] > 0:
                n+=1
                enemy[1] += enemy_speed
                xloc = int(((enemy[0] / 16)))
                xlocback = int(((enemy[0] / 16)-1))
                xlocforward = int(((enemy[0] / 16)+1))
                ylocup = int(((enemy[1] / 16)))
                yloc = int(((enemy[1] / 16)))+1
                ylocdown = int(((enemy[1] / 16)+2))

                rects = []
                if self.blocks[yloc][xloc] == 1:
                    rects.append(pygame.Rect((xloc*16, yloc*16),(16,16)))
                if self.blocks[ylocdown][xloc] == 1:
                    rects.append(pygame.Rect((xloc*16, ylocdown*16),(16,16)))
                if self.blocks[yloc][xlocback] == 1:
                    rects.append(pygame.Rect((xlocback*16, yloc*16),(16,16)))
                if self.blocks[ylocdown][xlocback] == 1:
                    rects.append(pygame.Rect((xlocback*16, ylocdown*16),(16,16)))
                if self.blocks[yloc][xlocforward] == 1:
                    rects.append(pygame.Rect((xlocforward*16, yloc*16),(16,16)))
                if self.blocks[ylocdown][xlocforward] == 1:
                    rects.append(pygame.Rect((xlocforward*16, ylocdown*16),(16,16)))
                for rect in rects:
                    if rect.collidepoint(enemy[0]+8, enemy[1]+16):
                        enemy[1] = rect.top-16

                if enemy[2] == 0:
                    rects = []
                    if self.blocks[yloc][xloc] == 1:
                        rects.append(pygame.Rect((xloc*16, yloc*16),(16,16)))
                    if self.blocks[ylocdown][xloc] == 1:
                        rects.append(pygame.Rect((xloc*16, ylocdown*16),(16,16)))
                    if self.blocks[ylocup][xloc] == 1:
                        rects.append(pygame.Rect((xloc*16, ylocup*16),(16,16)))
                    if self.blocks[yloc][xlocback] == 1:
                        rects.append(pygame.Rect((xlocback*16, yloc*16),(16,16)))
                    if self.blocks[ylocdown][xlocback] == 1:
                        rects.append(pygame.Rect((xlocback*16, ylocdown*16),(16,16)))
                    if self.blocks[ylocup][xlocback] == 1:
                        rects.append(pygame.Rect((xlocback*16, ylocup*16),(16,16)))
                    enemy[0] -= enemy_speed
                    for rect in rects:
                        if rect.colliderect(pygame.Rect(enemy[0],enemy[1],16,16)):
                            enemy[0] = rect.right
                            enemy[2] = 1
                else:
                    rects = []
                    if self.blocks[yloc][xloc] == 1:
                        rects.append(pygame.Rect((xloc*16, yloc*16),(16,16)))
                    if self.blocks[ylocdown][xloc] == 1:
                        rects.append(pygame.Rect((xloc*16, ylocdown*16),(16,16)))
                    if self.blocks[ylocup][xloc] == 1:
                        rects.append(pygame.Rect((xloc*16, ylocup*16),(16,16)))
                    if self.blocks[yloc][xlocback] == 1:
                        rects.append(pygame.Rect((xlocback*16, yloc*16),(16,16)))
                    if self.blocks[ylocdown][xlocback] == 1:
                        rects.append(pygame.Rect((xlocback*16, ylocdown*16),(16,16)))
                    if self.blocks[ylocup][xlocback] == 1:
                        rects.append(pygame.Rect((xlocback*16, ylocup*16),(16,16)))
                    enemy[0] += enemy_speed
                    for rect in rects:
                        if rect.colliderect(pygame.Rect(enemy[0],enemy[1],16,16)):
                            enemy[0] = rect.left-16
                            enemy[2] = 0

    def collideEnemies(self):
        mario_rect = pygame.Rect(120,self.mario_loc[0],16,16)
        temp_e = deepcopy(self.enemies)
        for i, enemy in enumerate(self.enemies):
            if mario_rect.colliderect(pygame.Rect(enemy[0]-self.offset,enemy[1],16,16)):
                if not self.mario_loc[4]:
                    del temp_e[i]
                    self.mario_loc[3] = -4
                else:
                    self.dead = True
        self.enemies = deepcopy(temp_e)

    def updateScreen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                exit()
        if self.show:
            self.screen.fill((0,0,0))

        self.block_rects = []

        self.offset = self.mario_loc[1] - 120
        for x in range(len(self.blocks[0])):
            for y in range(len(self.blocks)):
                if self.blocks[y][x] == 1:
                    self.block_rects.append(pygame.Rect(x*16 - self.offset,y*16,16,16))
        if self.show:
            for r in self.block_rects:
                pygame.draw.rect(self.screen, (255,255,255), r)
           
            #draw mario
            pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(120,self.mario_loc[0],16,16))
            
            for enemy in self.enemies:
                pygame.draw.rect(self.screen, (0,0,255), pygame.Rect(enemy[0]-self.offset,enemy[1],16,16))

            pygame.display.flip()
        self.run_once = True

if __name__ == '__main__':
    level1 = MarioLevel()
    while 1:
        level1.acceptInputHuman();