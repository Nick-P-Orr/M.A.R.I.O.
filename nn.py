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
    max_x = 0

    def __init__(self):
        self.comm = Communicator()

    def initial_population(self):
        for i in range(10):
            self.models.append(self.generate_model()) #generate 5 initial models

    def generate_model(self):
        model = []
        for i in range(10): #between 1 and 5 connections
            trigger = randint(0,4) #0 for always, 1-3 for block, (not implemented->) 2 for enemy
            if trigger == 0: #don't need to choose a location
                command = randint(0,3) #choose which command
                model.append([trigger, command, -1])
            else: #must choose a location to connect it to
                location = [randint(0,13), randint(0,15)]
                command = randint(0,3)
                model.append([trigger, command, location])
        return model

    def compile_commands(self, grid, model):
        commands = []
        for connection in model:
            if connection[0] == 0:
                if connection[1] not in commands:
                    commands.append(connection[1])
            else:
                try:
                    if grid[connection[2][0]][connection[2][1]] == connection[0]:
                        if connection[1] not in commands:
                            commands.append(connection[1])
                except:
                    print('broke')
                    print(grid)
                    print(connection)
                    exit()
        return commands

    def checkStuck(self, l):
        if l <= self.max_x:
            return True
        max_x = l
        return False

    def test_models(self):
        self.last_models = []
        for model in self.models[-9:]:
            self.comm.newLevel()
            response = self.comm.passInput(None)
            grid = response[1]
            done = False
            prev_scores = [0]
            while not done:
                commands = self.compile_commands(grid, model)
                response = self.comm.passInput(commands)
                response[0] -= 120
                done = response[2]
                grid = response[1]
                if response[0] >= 0:
                    prev_scores.append(response[0])
                    if self.checkStuck(prev_scores[-1]):
                        self.last_models.append([model, prev_scores[-1]])
                        done = True
                else:
                    self.last_models.append([model, prev_scores[-1]])
                    done = True


    def model(self):
        network = input_data(shape=[None, 10, 1], name='input')
        network = fully_connected(network, 25, activation='relu')
        network = fully_connected(network, 1, activation='linear')
        network = regression(network, optimizer='adam', learning_rate=1e-2, loss='mean_square', name='target')
        model = tflearn.DNN(network)
        return model

    def preprocess_data(self, data):
        processed_data = []
        for pop in data:
            processed_pop = []
            for connection in pop[0]:
                new_value = str(connection[0])+str(connection[1])
                if connection[2] == -1:
                    new_value += ('.1717')
                else:
                    new_value += '.'
                    for i in connection[2]:
                        new_value += (str(i))
                processed_pop.append(float(new_value))
            processed_data.append([processed_pop, pop[1]])
        return processed_data

    def preprocess_data2(self, data): #digs into array less because new prediction data doe not have outputs
        processed_data = []
        for connection in data:
            new_value = str(connection[0])+str(connection[1])
            if connection[2] == -1:
                new_value += ('.1717')
            else:
                new_value += '.'
                for i in connection[2]:
                    new_value += (str(i))
            processed_data.append(float(new_value))
        return processed_data

    def train_model(self, training_data, model):
        X = np.array([i[0] for i in training_data]).reshape(-1, 10, 1)
        y = np.array([i[1] for i in training_data]).reshape(-1, 1)
        model.fit(X,y, n_epoch = 3, shuffle = True, run_id = 'test', show_metric=True)
        model.save('test')
        return model

    def predict_new_models(self, model):
        unprocessed = []
        new_models = []
        for i in range(20):
            m = self.generate_model()
            unprocessed.append(m)
            m = self.preprocess_data2(m)
            m = np.array(m).reshape(-1,10,1)
            new_models.append(m)
        results = []
        for i, m in enumerate(new_models):
            results.append((unprocessed[i], model.predict(m)[0][0]))
        return results

    def getScore(self, val):
        return val[1]

    def chooseNew(self, predictions):
        predictions.sort(key=self.getScore)
        chosen = predictions[0:10]
        chosen = [i[0] for i in chosen]
        for i in chosen:
            self.models.append(i)


m = MarioNN()
m.initial_population()
m.test_models()
sum=0
for i in m.last_models:
    sum+=i[1]
print("Random Avg: "+str(sum/10))

mod = m.model()
for x in range(100):
    print(len(m.last_models))
    training_data = m.preprocess_data([m.models])
    trained = m.train_model(training_data, mod)
    predictions = m.predict_new_models(trained)
    m.chooseNew(predictions)
    m.test_models()


sum=0
for i in m.last_models:
    sum+=i[1]
print("Learned Avg: "+str(sum/10))
print(m.last_models)



