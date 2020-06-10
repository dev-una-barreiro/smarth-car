import tensorflow as tf
import pandas as pd
import numpy as np
import csv


class CreateNeural:

    model: tf.keras.Sequential
    file_path = 'F:/Projetos/smarth-car/project/packages/tensorML/data.csv'

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
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='softmax', input_shape=[
                len(dataset.keys())]),
            tf.keras.layers.Dense(32, activation='softmax'),
            tf.keras.layers.Dense(1)
        ])
        self.model.compile(optimizer='adam',
                           loss=tf.keras.losses.BinaryCrossentropy(
                               from_logits=True),
                           metrics=['accuracy'])

        self.model.fit(dataset, labels)

    def predictValue(self, value: list):
        result = self.model.predict(value)
        print(result)
        max_value = round(np.amax(result))
        max_index_col = np.argmax(result)

        to_write = value[max_index_col]

        to_write.append(max_value)

        self.write_cvs(to_write)
        return max_value

    def write_cvs(self, value):
        list_string = ''.join([str(f'{elem},') for elem in value])
        with open(self.file_path, 'a') as fd:
            fd.write(f'\n{list_string[:-1]}')


model = CreateNeural()
