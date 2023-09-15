"""
module start all the threads and thier objects.
"""
import time
import cv2
from video_get import VideoGet
from video_show import VideoShow
from counts_per_sec import CountsPerSec
from emotion_detection import VideoClassify
from utils.data_land_marker import LandMarker
from utils.image_classifier import ImageClassifier
from keras.models import load_model

model = load_model('models/model_emotion.h5')
PREDICTOR_PATH = 'models/shape_predictor_68_face_landmarks.dat'
face_detect = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
land_marker = LandMarker(landmark_predictor_path = PREDICTOR_PATH)
classifier = ImageClassifier(land_marker = land_marker)

def main_thread(video_url: str):
    """
    main_thread module take video_url as input.

    Parameters
    ----------
    video_url: str
        youtube video url.
    
    Return
    ------
    video_getter: object
        VideoGet class object thread.
    video_classifier: object
        VideoClassify class object thread.
    count_p_second: object
        CountsPerSec class object thread.
    """
    video_getter = VideoGet(video_url).start()
    video_classifier = VideoClassify(model, classifier, face_detect,
                                    video_getter.frame).start()
    time.sleep(5)
    # video_shower = VideoShow(video_classifier.frame).start()
    count_p_second = CountsPerSec().start()
    return video_getter, video_classifier, count_p_second
