# 🚗 Driver Drowsiness Detection System

A Computer Vision and Deep Learning project to detect driver drowsiness using yawning detection.

---

## 📌 Overview

Drowsy driving is a major cause of road accidents. This project aims to detect signs of driver fatigue by analyzing facial behavior, specifically yawning.

The system uses a Convolutional Neural Network (CNN) trained on yawning and non-yawning images to classify whether a driver is drowsy.

---

## 🚀 Features

- 😮 Yawning detection using Deep Learning (CNN)
- 📸 Image-based prediction via web app
- 🌐 Deployable using Streamlit
- ⚡ Lightweight and fast inference
- 🧠 High accuracy (~95%)

---

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Streamlit

---


---

## ⚙️ How the System Works

### 🔹 Step 1: Image Upload
User uploads an image using the Streamlit interface.

### 🔹 Step 2: Image Preprocessing
- Image is resized to **224x224**
- Pixel values normalized (0–1)
- Converted into model input format

### 🔹 Step 3: Model Prediction
- CNN model predicts:
  - `No Yawn`
  - `Yawn`
- Output is a probability score

### 🔹 Step 4: Decision Logic
- If **yawn probability > 0.6**
  → 🚨 DROWSY
- Else
  → ✅ NOT DROWSY

---

## 🧪 Model Details

- Architecture: CNN (Transfer Learning possible)
- Input Size: 224x224
- Output: Binary Classification (Yawn / No Yawn)
- Training Accuracy: ~95%
- Validation Accuracy: ~95%

---

## 📊 Dataset

The model was trained on a yawning dataset containing labeled images.

You can use similar datasets:

- Yawn Dataset (Kaggle)
- MRL Eye Dataset

(Note: Dataset is not included due to size limitations)

---

## ▶️ How to Run Locally

pip install -r requirements.txt
streamlit run streamlit_app.py

🌐 Deployment

This project can be deployed using Streamlit Cloud.

## ⚠️ Limitations

This version uses only yawning detection
Does not include eye tracking (EAR)
Performance depends on image quality

## 🔮 Future Improvements

👁️ Eye detection using EAR (dlib)
🎥 Real-time webcam detection
🧠 Temporal models (LSTM)
🌙 Night-time detection

## 👨‍💻 Author

Abdul Haseeb
