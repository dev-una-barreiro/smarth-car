from project.packages.env import currentEnv
from tensorflow import keras
import pandas as pd
import numpy as np
import csv


class CreateNeural:

    model: keras.Sequential
    file_path = currentEnv['csvPath']

    def __init__(self):
        self._create_model()

    def _load_training_csv(self):
        raw_dataset = pd.read_csv(
            self.file_path)
        dataset = raw_dataset.copy()

        return dataset

    def _create_model(self):
        dataset = self._load_training_csv()
        labels = dataset.pop('resultado')
        self.model = keras.Sequential([
            keras.layers.Dense(32, activation='softmax', input_shape=[
                len(dataset.keys())]),
            keras.layers.Dense(1)
        ])
        self.model.compile(optimizer='adam',
                           loss='mean_squared_error',
                           metrics=['accuracy'])
        self.model.fit([dataset], labels)

    def predictValue(self, value):
        result = self.model.predict(value)
        max_value = round(np.amax(result))
        max_index_col = np.argmax(result)
        to_write = np.array([*value[max_index_col], max_value])
        print(to_write)
        # self.write_cvs(to_write)
        return max_value

    def write_cvs(self, value):
        list_string = ''.join([str(f'{elem},') for elem in value])
        with open(self.file_path, 'a') as fd:
            fd.write(f'\n{list_string[:-1]}')


model = CreateNeural()
