from Communicator import Communicator 
from random import randint
import numpy as np
import tflearn
import math
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.estimator import regression
from statistics import mean
import time

class MarioNN:
    comm = None
    models = []
    last_models = []
    commands = ['left', 'right', 'run', 'jump']

    def __init__(self):
        self.comm = Communicator()

    def initial_population(self):
        for i in range(10):
            self.models.append(self.generate_model()) #generate 5 initial models

    def generate_model(self):
        model = []
        for i in range(randint(1,5)): #between 1 and 5 connections
            trigger = randint(0,1) #0 for always, 1 for block, (not implemented->) 2 for enemy
            if trigger == 0: #don't need to choose a location
                command = self.commands[randint(0,3)] #choose which command
                model.append([trigger, command, -1])
            else: #must choose a location to connect it to
                location = [randint(0,15), randint(0,15)]
                command = self.commands[randint(0,3)]
                model.append([trigger, command, location])
        return model

    def compile_commands(self, grid, model):
        commands = []
        for connection in model:
            if connection[0] == 0:
                if connection[1] not in commands:
                    commands.append(connection[1])
            else:
                if grid[connection[2][0]][connection[2][1]] == connection[0]:
                    if connection[1] not in commands:
                        commands.append(connection[1])
        return commands

    def checkEqual(self, l):
        for i in l:
            if i != l[0]:
                return False
        return True

    def test_models(self):
        self.last_models = []
        for model in self.models:
            self.comm.newLevel()
            response = self.comm.passInput(None)
            grid = response[1]
            done = False
            prev_scores = [0]
            while not done:
                commands = self.compile_commands(grid, model)
                response = self.comm.passInput(commands)
                response[0] -= 120
                grid = response[1]
                if response[0] >= 0:
                    prev_scores.append(response[0])
                    if len(prev_scores) > 15:
                        if self.checkEqual(prev_scores[-15:]):
                            self.last_models.append((model, prev_scores[-1]))
                            done = True
                else:
                    self.last_models.append((model, prev_scores[-1]))
                    done = True
                time.sleep(.05)
            print(self.last_models[-1][1])
            time.sleep(.25)

m = MarioNN()
m.initial_population()
m.test_models()
print(m.last_models)

