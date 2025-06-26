from tensorflow.keras.models import load_model
import librosa
import numpy as np
import os

emotions = os.listdir('Emotions')
print("Testing::emotions", emotions)

# Load the model
print("Testing::loding model-")
model = load_model('emotion_detection_better.h5')

# Load the audio file
print("Testing::loading audio file")
audio_path = 'Fear.wav'
y, sr = librosa.load(audio_path, sr=None)  # sr=None keeps the original sample rate

# Extract MFCCs (example feature extraction)
print("Testing::MFCCs")
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

mfccs = np.mean(mfccs.T, axis=0)  # Take the mean for a fixed-size input
# Reshape for a single sample (batch size of 1)
print("Testing::Reshape")
input_features = np.expand_dims(mfccs, axis=0)

# Predict emotion
print("Predicting Model Working")
predictions = model.predict(input_features)
emotion = np.argmax(predictions)  # Get the class with the highest probability
print(f'Predicted Emotion: {emotions[int(emotion)]}')
