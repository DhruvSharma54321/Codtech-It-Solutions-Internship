# Speech Emotion Recognition - Sound Classification

## Overview
This Jupyter Notebook focuses on Speech Emotion Recognition (SER) by classifying audio clips into different emotional categories such as Angry, Happy, Sad, Fearful, Disgusted, Neutral, and Surprised. The project involves loading and analyzing a dataset of speech samples, performing exploratory data analysis (EDA), and visualizing audio waveforms and spectrograms to understand the characteristics of different emotions.

## Features
- **Data Loading**: The dataset consists of 12,797 audio files categorized into 7 emotions.
- **Exploratory Data Analysis (EDA)**: Includes visualizations like count plots to show the distribution of emotions in the dataset.
- **Audio Visualization**: Functions to display waveforms and spectrograms for different emotional categories.
- **Feature Extraction**: Utilizes the `librosa` library to analyze audio features.

## Dataset
The dataset is structured with the following emotion distribution:
- Happy: 2167 samples
- Sad: 2167 samples
- Angry: 2166 samples
- Fearful: 2047 samples
- Disgusted: 1863 samples
- Neutral: 1795 samples
- Surprised: 592 samples

## Dependencies
- pandas
- numpy
- os
- seaborn
- matplotlib
- librosa
- IPython.display

## Usage
1. **Import Modules**: Load necessary libraries for data manipulation, visualization, and audio processing.
2. **Load the Dataset**: Read audio file paths and labels into a DataFrame.
3. **Exploratory Data Analysis**: Analyze the distribution of emotions and visualize the dataset.
4. **Audio Visualization**: Use `waveplot` and `spectrogram` functions to visualize audio samples for different emotions.

## Functions
- `waveplot(data, sr, emotion)`: Plots the waveform of an audio sample.
- `spectrogram(data, sr, emotion)`: Displays the spectrogram of an audio sample.

## Example
```python
# Example usage of waveplot and spectrogram
emotion = 'Angry'
audio_path = df[df['label'] == emotion]['speech'].iloc[0]
data, sr = librosa.load(audio_path)
waveplot(data, sr, emotion)
spectrogram(data, sr, emotion)
```

## Future Work
- Implement machine learning models for emotion classification.
- Extract more advanced audio features (e.g., MFCCs, chroma features).
- Optimize the model for better accuracy.

## Author
Dhruv

## License
This project is open-source and available for public use.