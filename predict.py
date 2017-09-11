from keras.layers import Input, Dense
from keras.models import models
import numpy as np
import pandas as pd 
# # tensors
# inputs = Input(shape=(784,))

# # layer instance
# x = Dense(64, activation='relu')(inputs)
# x = Dense(64, activation='relu')(x)
# x = Dense(64, activation='relu')(x)

# predictions = Dense(10, activation='softmax')(x)

model = Sequential()

model.add(Dense(12, input_dim=8, activation='relu'))

model = Model(inputs=inputs, outputs=predictions)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(data, labels)
