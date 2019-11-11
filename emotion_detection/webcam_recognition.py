import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub
import sys
from constants import *
from redislite import Redis

MODEL_FILE = "emotion_detection/models/model6v2.hdf5"
IMAGE_SIZE = 224

EXPRESSIONS = sorted([
    "Negative", "Neutral", "Positive", "Uncertain"
])

#Load the saved model
model = tf.keras.models.load_model(MODEL_FILE, custom_objects={'KerasLayer':hub.KerasLayer})
video = cv2.VideoCapture(0)

r = Redis(REDIS_DB_FILE)

while True:
        _, frame = video.read()

        #Convert the captured frame into RGB
        im = Image.fromarray(frame, 'RGB')

        #Resizing into 224x224 because we trained the model with this image size.
        im = im.resize((IMAGE_SIZE,IMAGE_SIZE))
        img_array = np.array(im) / 255
        img_array = np.expand_dims(img_array, axis=0)

        pred_array = model.predict(img_array)
        prediction = np.argmax(pred_array[0])


        r.publish(UI_CHANNEL, EXPRESSIONS[prediction])
        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()
