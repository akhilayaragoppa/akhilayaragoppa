# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:48:25 2020

@author: akhila
"""


import tensorflow as tf
from tensorflow import keras

import pandas as pd
import numpy as np


train_df = pd.read_csv('./data/train.csv')
np.random.shuffle(train_df.values)
print(train_df.tail())

model = keras.Sequential([
    keras.layers.Dense(32,input_shape=(2,),activation = 'relu'),
    keras.layers.Dense(2, activation = 'softmax')])

model.compile(optimizer='adam',
              loss= keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy']
              )

x = np.column_stack((train_df.x.values, train_df.y.values))

model.fit(x,train_df.color.values, batch_size = 10, epochs=10)

print('\nEVALUATION')
test_df = pd.read_csv('./data/test.csv')
test_x = np.column_stack((test_df.x.values, test_df.y.values))

model.evaluate(test_x, test_df.color.values)