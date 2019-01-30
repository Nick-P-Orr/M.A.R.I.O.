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
block_rects = []

#            y,  x, xs, ys, grounded, jump start speed
mario_loc = [208,48, 0, 0, True, 0]

done = False
run_once = False

def acceptInput(mario_loc, block_rects):
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
                mario_loc = handlePhysics(mario_loc, keypress, block_rects)
                return mario_loc

def handlePhysics(mario_loc, keypress, block_rects):
    min_speed = 1.1875
    walk_accel = 0.59375
    run_accel = 0.890625
    release_decel = -0.8125
    skid_decel = -1.625
    max_run_speed = 41
    skid_turnaround_speed = 9

    jump_speed = [-4, -4, 80/16]
    jumping_gravity = [2/16, 1.875/16, 2.5/16]
    falling_gravity = [7/16, 6/16, 9/16]

    air_forward_speed = [0.59375, 0.890625]
    air_backward_speed = [-0.890625, -0.8125, -0.59375]

    mario_rect = pygame.Rect(mario_loc[1],mario_loc[0],16,16)

    if mario_loc[4]:
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
    else:
        if 'right' in keypress and not 'left' in keypress and mario_loc[2] < max_run_speed:
            if mario_loc[2] >= 0:
                if mario_loc[2] < 25:
                    mario_loc[2] += air_forward_speed[0]
                else:
                    mario_loc[2] += air_forward_speed[1]
            else:
                if mario_loc[2] >= 25:
                    mario_loc[2] += air_backward_speed[0]
                elif mario_loc[2] < 25:
                    if mario_loc[5] >= 29:
                        mario_loc[2] += air_backward_speed[1]
                    else:
                        mario_loc[2] += air_backward_speed[2]

        if 'left' in keypress and not 'right' in keypress and mario_loc[2] > max_run_speed*-1:
            if mario_loc[2] <= 0:
                if mario_loc[2] > -25:
                    mario_loc[2] -= air_forward_speed[0]
                else:
                    mario_loc[2] -= air_forward_speed[1]
            else:
                if mario_loc[2] <= -25:
                    mario_loc -= air_backward_speed[0]
                elif mario_loc[2] > -25:
                    if mario_loc[5] <= -29:
                        mario_loc[2] -= air_backward_speed[1]
                    else:
                        mario_loc[2] -= air_backward_speed[2]
    if 'jump' in keypress:
        if mario_loc[2] > -16 and mario_loc[2] < 16:
            if mario_loc[4]:
                mario_loc[3] = jump_speed[0]
                mario_loc[5] = mario_loc[2]
            else:
                mario_loc[3] += jumping_gravity[0]
        elif abs(mario_loc[2]) >= -16 and abs(mario_loc[2]) < 36.99609375:
            if mario_loc[4]:
                mario_loc[3] = jump_speed[1]
            else:
                mario_loc[3] += jumping_gravity[1]
        else:
            if mario_loc[4]:
                mario_loc[3] = jump_speed[2]
            else:
                mario_loc[3] += jumping_gravity[2]
    elif not mario_loc[4]:
        if mario_loc[2] > -16 and mario_loc[2] < 16:
            mario_loc[3] += falling_gravity[0]
        elif abs(mario_loc[2]) >= -16 and abs(mario_loc[2]) < 36.99609375:
            mario_loc[3] += falling_gravity[1]
        else:
            mario_loc[3] += falling_gravity[2]

    mario_loc[1] += mario_loc[2]
    for rect in block_rects:
        if mario_rect.colliderect(pygame.Rect(rect.left-mario_loc[2], rect.top, rect.width+(2*mario_loc[2]), rect.height)):
            if mario_loc[2] > 0:
                mario_loc[1] = rect.left-16
                mario_loc[2] = 0
            else:
                mario_loc[1] = rect.right+1
                mario_loc[2] = 0
    mario_loc[0] += mario_loc[3]
    flag = 0
    hit_rect = None
    for rect in block_rects:
        if mario_rect.colliderect(pygame.Rect(rect.left, rect.top-mario_loc[3], rect.width, rect.height+mario_loc[3])) and mario_loc[3] > 0:
            flag = 1
            hit_rect = rect
        elif mario_rect.colliderect(pygame.Rect(rect.left, rect.top-1, rect.width, rect.height+1)) and mario_loc[3] == 0:
            flag = 2
            hit_rect = rect

    if flag > 0:
        if flag == 1:
            mario_loc[3] = 0
            mario_loc[0] = hit_rect.top-16
        mario_loc[4] = True
    else:
        mario_loc[4] = False

    return mario_loc



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            exit()
    if run_once:
        mario_loc = acceptInput(mario_loc, block_rects)

    screen.fill((0,0,0))
    #draw blocks
    block_rects = []
    for x in range(len(visual[0])):
        for y in range(len(visual)):
            if visual[x][y] == 1:
                block_rects.append(pygame.Rect(y*16,x*16,16,16))
    for r in block_rects:
        pygame.draw.rect(screen, (255,255,255), r)
    #draw mario
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(mario_loc[1],mario_loc[0],16,16))

    pygame.display.flip()
    run_once = True