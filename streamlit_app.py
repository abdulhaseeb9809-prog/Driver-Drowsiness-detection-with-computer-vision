import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# ---------------- LOAD MODEL ----------------
model = load_model("yawn_classifier.h5")

# ---------------- UI ----------------
st.title("🚗 Driver Drowsiness Detection")
st.write("Upload an image to detect drowsiness (Yawning Detection)")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

# ---------------- PROCESS ----------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = np.array(image)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Prediction
    pred = model.predict(img)[0]

    # Assuming: [no_yawn, yawn]
    yawn_prob = pred[1]

    st.write(f"### 😮 Yawn Probability: {yawn_prob:.2f}")

    # Decision
    if yawn_prob > 0.6:
        st.error("🚨 DROWSY (Yawning Detected)")
    else:
        st.success("✅ NOT DROWSY")
