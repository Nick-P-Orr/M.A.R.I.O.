import pygame
import numpy

pygame.init()
size = width, height = 256,256
screen = pygame.display.set_mode((size))
#0 is nothing, 1 is blocks
blocks = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
visual = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
mario_loc = [208,48, 0, 0]

done = False
run_once = False

def acceptInput(mario_loc):
    keypress = []
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    keypress.append('left')
                if event.key == pygame.K_RIGHT:
                    keypress.append('right')
                if event.key == pygame.K_LCTRL:
                    keypress.append('run')
                if event.key == pygame.K_SPACE:
                    keypress.append('jump')
                mario_loc = handlePhysics(mario_loc, keypress)
                return mario_loc

def handlePhysics(mario_loc, keypress):
    min_speed = 1.1875
    walk_accel = 0.5625
    run_accel = .875
    release_decel = -0.8125
    skid_decel = -1.625
    max_run_speed = 41
    skid_turnaround_speed = 9

    jump_speed = [-64, -64, 80]
    jumping_gravity = [2, 1.875, 2.5]
    falling_gravity = [7, 6, 9]

    if 'right' in keypress and not 'left' in keypress and mario_loc[2] < max_run_speed:
        if mario_loc[2] < 0 and mario_loc[2] > skid_turnaround_speed * -1:
            mario_loc[2] *= -1
        elif mario_loc[2] < 0:
                mario_loc[2] -= skid_decel
        elif mario_loc[2] == 0:
            mario_loc[2] = min_speed
        elif 'run' in keypress:
            mario_loc[2] += run_accel
        else:
            mario_loc[2] += walk_accel

    elif 'left' in keypress and not 'right' in keypress and mario_loc[2] > max_run_speed * -1:
        if mario_loc[2] > 0 and mario_loc[2] < skid_turnaround_speed:
            mario_loc[2] *= -1
        elif mario_loc[2] > 0:
                mario_loc[2] += skid_decel
        elif mario_loc[2] == 0:
            mario_loc[2] = min_speed * -1
        elif 'run' in keypress:
            mario_loc[2] -= run_accel
        else:
            mario_loc[2] -= walk_accel

    else:
        if mario_loc[2] > 0:
            mario_loc[2] += release_decel
        elif mario_loc[2] < 0:
            mario_loc[2] -= release_decel

    if 'jump' in keypress:
        if mario_loc[2] > -16 and mario_loc[2] < 16:
            mario_loc[3] = jump_speed[0]

    mario_loc[1] += mario_loc[2]
    mario_loc[0] += mario_loc[3]

    return mario_loc



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit()
    if run_once:
        mario_loc = acceptInput(mario_loc)

    screen.fill((0,0,0))
    #draw blocks
    for x in range(len(visual[0])):
        for y in range(len(visual)):
            if visual[x][y] == 1:
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(y*16,x*16,16,16))
    #draw mario
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(mario_loc[1],mario_loc[0],16,16))

    pygame.display.flip()
    run_once = True