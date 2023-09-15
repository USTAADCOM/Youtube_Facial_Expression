# Youtube_Facial_Expression 
Facial Emotion Detection From youtube video using Opencv and self trained model.
## Setup
  ```code
  conda create -n <env_name>
  conda activate <env_name>
  git clone https://github.com/USTAADCOM/Youtube_Facial_Expression.git
  cd Youtube_Facial_Expression
  pip install -r requirements.txt
  ```
## Model
  Download Model Link below
  [Here](https://drive.google.com/file/d/1PMAXq6mdzXYhJZZvmC39aj0XSsC5cCTq/view?usp=sharing)

## Project Structure
```bash
Youtube_Facial_Expression
│   counts_per_sec.py
│   emotion_detection.py
│   main_thread.py
│   requirements.txt
│   server.py
│   video_get.py
│   video_show.py
│
├───models
│       haarcascade_frontalface_default.xml
│       Keras_emotion_detection_model_training.ipynb
│       models.rar
│       model_emotion.h5
│       shape_predictor_68_face_landmarks.dat
│
├───templates
│       index.html
│       welcome.html
│───utils
    │   data_land_marker.py
    │   image_classifier.py
    │
```

## Run Flask Server
```code
python3 server.py
```
