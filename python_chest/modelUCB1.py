import seaborn as sns
import numpy as np
from numpy import *
from sklearn.cross_validation import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.regularizers import l2

from keras.utils import np_utils

labelsTrain = np_utils.to_categorical(y_train)
labelsTest = np_utils.to_categorical(y_test)
labelsDepy = np_utils.to_categorical(y_deploy)

model = Sequential()
model.add(Dense(20,
                input_shape=(3,),
                activation="relu"))
#model.add(Dropout(0.5))
model.add(Dense(8, activation="softmax"))



model.load_weights('chestModelbest.hdf5')


model.compile(loss='categorical_crossentropy',
              metrics=['accuracy'],
              optimizer='adam')
# Actual modelling

score, accuracy = model.evaluate(X_deploy, labelsDepy, batch_size=13, verbose=0)
print("Test fraction correct (NN-Score) = {:.2f}".format(score))
print("Test fraction correct (NN-Accuracy) = {:.2f}".format(accuracy))

####################################################
#n_samples ,_=Y_test.shape
SamplingTesting=500
All_weights=model.get_weights()
All_weights_BUCKUP = model.get_weights()
FC_weights_3=All_weights[0]
row,col= shape(FC_weights_3)
SizeWights=row*col
OldAccuracy = accuracy
