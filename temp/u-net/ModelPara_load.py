from keras.models import *
from keras.layers import *
from keras.optimizers import *
from keras import backend as keras
from keras.models import model_from_json


model = model_from_json(open('my_model_architecture.json').read())#read model architecture first
model.compile(optimizer=Adam(lr=1e-3), loss='binary_crossentropy', metrics=['accuracy'])
model.load_weights('my_model_weights.h5')#then, read weights
