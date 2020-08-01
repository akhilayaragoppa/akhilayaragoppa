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

color_dict = {'teal':0,'blue':1,'orange':2,'purple':3,'green':4,'red':5}
train_df.color = train_df.color.apply(lambda x: color_dict[x])

print(train_df.tail())
print(train_df.color.unique())



model = keras.Sequential([
    keras.layers.Dense(32,input_shape=(2,),activation = 'relu'),
    keras.layers.Dense(6, activation = 'sigmoid')])

model.compile(optimizer='adam',
              loss= keras.losses.SparseCategoricalCrossentropy(from_logits = True),
              metrics = ['accuracy']
              )

x = np.column_stack((train_df.x.values, train_df.y.values))

model.fit(x,train_df.color.values, batch_size = 10, epochs=10)

print('\nEVALUATION')
test_df = pd.read_csv('./data/test.csv')
test_df.color = test_df.color.apply(lambda x: color_dict[x])
test_x = np.column_stack((test_df.x.values, test_df.y.values))

model.evaluate(test_x, test_df.color.values)

print(np.round(model.predict([[-2.0,3.0]])))