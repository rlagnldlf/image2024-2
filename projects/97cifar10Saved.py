import tensorflow as tf
from tensorflow.keras.datasets import cifar10

(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

print(f'{train_images.shape=}, {train_labels.shape=}')
print(f'{test_images.shape=}, {test_labels.shape=}')

cnn_saved_model = tf.keras.models.load_model('cnn_model_working.h5')
cnn_saved_model.summary()
cnn_saved_model.evaluate()