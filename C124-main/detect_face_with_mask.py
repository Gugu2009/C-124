import cv2
import numpy as np
import tensorflow as tensorflow


model =tf.keras.models.load_model('keras_model.h5')

video = cv2.VideoCapture(0)