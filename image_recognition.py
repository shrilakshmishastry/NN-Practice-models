import tensorflow as tf
from tensorflow import  keras as ks

import numpy as np
from numpy import random,array
import matplotlib.pyplot as plt


def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, img = predictions_array, true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')



# importing and loading the datasets
fasion_mnist = ks.datasets.fashion_mnist
(train_image,train_labels), (test_image,test_labels) = fasion_mnist.load_data()
print(train_image[0])
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# reducing pixel values between 0-1
train_image = train_image/255.0
test_image = test_image/255.0

# models

models = ks.Sequential([
    ks.layers.Flatten(input_shape=(28,28)),
    ks.layers.Dense(128,activation="relu"),
    ks.layers.Dense(10)
])

models.compile(optimizer='adam',
        loss=ks.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy']
)

models.fit(train_image,train_labels,epochs=5)
plt.figure()
plt.imshow(test_image[9])
plt.colorbar()
plt.grid(False)
plt.show()
print(test_labels[9])

test_loss,test_acc = models.evaluate(test_image,test_labels,verbose=2)
predictions = models.predict(test_image)
print(predictions[0])

i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_image)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
plt.show()
