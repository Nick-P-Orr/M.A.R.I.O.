from MarioLevel1 import MarioLevel
from random import randint
import numpy as np
import tflearn
import math
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean
from collections import Counter

print('Hello')

class MarioNN:
    def __init__(self, initial_games = 10, test_games = 10, goal_steps = 5, lr = 1e-2, filename = 'mario_nn1.tflearn'):
#initial_games seems to be number of times run, but Im not sure about test_games
#I think goal_setps was originally how many steps the snake was supposed to move
#lr is a tensorflow value for learning_rate. Its recommended the further in training, the value is
#exponentially decayed.
        self.initial_games = initial_games
        self.test_games = test_games
        self.goal_setps = goal_steps
        self.lr = lr
        self.filename = filename
        self.vectors_and_keys = [
                [[-1, 0], 0],
                [[0, 1], 1],
                [[1, 0], 2],
                [[0, -1], 3]
                ]

        print('End of __init__')


    def initial_population(self):
        training_data = []
        #This should run mario the number of times set
        for _ in range(self.initial_games):
            game = MarioLevel()

    print('End of initial_population')


    #generate_action will randomly pick the next movement (originally -1,0,1 had an action in snake)
    def generate_action(self, ):
        action = randint(0,2) - 1

    print('End of generate_action')
