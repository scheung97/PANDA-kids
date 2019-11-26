import cv2
import numpy as np
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub
import sys
import math
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

# Load the Cascade Classifier Model
frontface_path = "emotion_detection/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(frontface_path)

show_video = False
if (sys.argv.length > 1 and sys.argv[1].lower() == 'true'):
    show_video = True

r = Redis(REDIS_DB_FILE)

while True:
        _, frame = video.read()

        # Convert captured frame to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=2)
        face_predictions = []
        for (x, y, w, h) in faces:
            if w < IMAGE_SIZE:
                if x < (IMAGE_SIZE/2):
                    x = 0
                else:
                    x = math.floor(x - ((IMAGE_SIZE - w) / 2))
                w = IMAGE_SIZE

            if h < IMAGE_SIZE:
                if y < (IMAGE_SIZE/2):
                    y = 0
                else:
                    y = math.floor(y - ((IMAGE_SIZE - h) / 2))
                h = IMAGE_SIZE

            if x + w > frame.shape[1]:
                x = frame.shape[1] - w

            if y + h > frame.shape[0]:
                y = frame.shape[0] - h

            # Crop to face
            cropped_frame = frame[y:y+h, x:x+w]

            try:
                im = Image.fromarray(cropped_frame, 'RGB')
            except ValueError:
                print("Weird PIL error, ignoring detection")
                continue

            #Resizing into 224x224 because we trained the model with this image size.
            # TODO: Consider excluding based on previous cropping?
            im = im.resize((IMAGE_SIZE,IMAGE_SIZE))
            img_array = np.array(im) / 255
            img_array = np.expand_dims(img_array, axis=0)

            pred_array = model.predict(img_array)
            prediction = np.argmax(pred_array[0])
            face_predictions.append(EXPRESSIONS[prediction])

            if show_video:
                frame = cv2.putText(frame, EXPRESSIONS[prediction], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        for p in face_predictions:
            r.publish(UI_CHANNEL, EXPRESSIONS[p])
        if show_video:
            cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()
