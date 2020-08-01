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
onehot_color = pd.get_dummies(train_df.color)
onehot_marker = pd.get_dummies(train_df.marker)
labels = np.hstack((onehot_color,onehot_marker))

print(train_df.head())
print(labels[0])


model = keras.Sequential([
    keras.layers.Dense(256,input_shape=(2,),activation = 'relu'),
    keras.layers.Dense(128,activation = 'relu'),
    keras.layers.Dense(128,activation = 'relu'),
    keras.layers.Dense(9, activation = 'sigmoid')])

model.compile(optimizer='adam',
              loss= keras.losses.BinaryCrossentropy(from_logits = True),
              metrics = ['accuracy']
              )

x = np.column_stack((train_df.x.values, train_df.y.values))

np.random.RandomState(seed=37).shuffle(x)
np.random.RandomState(seed=37).shuffle(labels)
model.fit(x,labels, batch_size = 10, epochs=5)

print('\nEVALUATION')
test_df = pd.read_csv('./data/test.csv')
test_x = np.column_stack((test_df.x.values, test_df.y.values))
onehot_color = pd.get_dummies(test_df.color)
onehot_marker = pd.get_dummies(test_df.marker)
test_labels = np.hstack((onehot_color,onehot_marker))

model.evaluate(test_x, test_labels)

print(np.round(model.predict([[-2,5],[0,5],[-2,3],[0.5,2.1]])))