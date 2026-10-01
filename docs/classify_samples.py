"""Classify every image in Sample_Images/ with the trained model. Run from the repo root: python docs/classify_samples.py"""
import os

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

CLASSES = ["APPLES", "BANANA", "ORANGE", "PINEAPPLE", "WATERMELON"]
model = load_model("nutrition.h5")

for name in sorted(os.listdir("Sample_Images")):
    img = image.load_img(os.path.join("Sample_Images", name), target_size=(64, 64))
    x = np.expand_dims(image.img_to_array(img) / 255.0, axis=0)  # same 1/255 rescale as training
    probs = model.predict(x, verbose=0)[0]
    i = int(np.argmax(probs))
    print(f"{name:<18} → {CLASSES[i]:<11} {probs[i] * 100:5.1f}%")
