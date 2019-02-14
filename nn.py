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

            prev_observation = self.generate_observation()


    print('End of initial_population')
    return training_data



    def generate_action():
        #My current thinking with generating an action is to
        #Have a running movement and normal movement just be set values
        #ie 2 is move right, 4 is move right with run pressed
        action = randint(0,5) - 1
        return action, self.get_game_action()


    def model(self):
        network = input_data(shape=[None, 4, 1], name='input')
        network = fully_connected(network, 1, activation='linear')
        network = regression(network, optimizer='adam', learning_rate=self.lr, loss='mean_square', name='target')
        model = tflearn.DNN(network, tensorboard_dir='log')
        return model

    def train_model(self, training_data, model):
        X = np.array([i[0] for i in training_data]).reshape(-1, 4, 1)
        y = np.array([i[1] for i in training_data]).reshape(-1, 1)
        model.fit(X,y, n_epoch = 1, shuffle = True, run_id = self.filename)
        model.save(self.filename)
        return model

    def test_model(self, model):
        steps_arr = []

    def train(self):
        training_data = self.initial_population()
        nn_model = self.model()
        nn_model = self.train_model(training_data, nn_model)
        self.test_model(nn_model)

    def visualise(self):
        nn_model = self.model()
        nn_model.load(self.filename)
        self.visualise_game(nn_model)

    def test(self):
        nn_model = self.model()
        nn_model.load(self.filename)
        self.test_model(nn_model)

    if __name__ == "__main__":
        MarioNN().train()
