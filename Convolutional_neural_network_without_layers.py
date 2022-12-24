import tensorflow as tf
from keras import layers
from keras import models as KM
from keras.datasets import mnist

#Extracting data from the dataset
mnist_dataset=tf.keras.datasets.mnist
#Creating the training and the test sets.
(training_images,training_labels), (testing_images,testing_labels)=mnist_dataset.load_data()
#Normalising the data
training_images , testing_images = training_images/255.0 , testing_images/255.0

#Feed_Forward_Model
#Giving input of images that have height and width 28*28
ip = layers.Input(shape=(28, 28))
#Flatenning the image                      
layer_1 = layers.Flatten()(ip)                              
layer_2 = layers.Dense(512, activation=tf.nn.relu)(layer_1)            
op = layers.Dense(10, activation=tf.nn.softmax)(layer_2)

model = KM.Model(ip, op)
model.summary()
model.compile(optimizer="adam",
                loss="sparse_categorical_crossentropy",
                metrics=["accuracy"])
model.fit(training_images, training_labels, epochs=10)
model.evaluate(training_images, training_labels)