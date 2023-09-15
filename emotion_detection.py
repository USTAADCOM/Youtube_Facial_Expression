"""
module for feature extraction and prediction for emotion detction
"""
from threading import Thread
import cv2
import numpy as np
# colors
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (255, 255, 104)
labels_dict = {0:'Angry',1:'Disgust', 2:'Fear', 3:'Happy',4:'Neutral',5:'Sad',6:'Surprise'}
landmark_points_list = [[(0, 0)]]

def draw_landmark_points(points: np.ndarray, img, color = BLUE_COLOR):
    """
    method take the 68 points array and draw over the image
    with specifief color.

    Parameters
    ----------
    points: array
        array of 68 points represeting face features Nose, Mouth etc.
    img: Image
        origional frame image 
    color: Tuple
        color of the face landmark.

    Return
    ------
    None 
        if no points provided for face over the image.
    """
    if points is None:
        return None
    for (x_axis, y_axis) in points:
        cv2.circle(img, (x_axis, y_axis), 1, color, -1)

class VideoClassify:
    """
    Class that perfomr emotion detection on frames.

    Attributes
    ----------
    frame : ndarray
        frame return by the video_get module.
    stopped : bool
        thread start or stop check.
    fps: float
        frame per second.
    Methods
    -------
    start():
        start the thread for CountsPerSec class.
    (): 
        display frames after emotion detection.
    stop():
        method to stop the thread.
    """
    def __init__(self, model, classifier,
                face_detect, frame = None):
        self.frame = frame
        self.model = model
        self.classifier = classifier
        self.face_detect = face_detect
        self.stopped = False
        self.frame_per_second = 1/30
    def start(self):
        """
        method start the threads for detection.

        Parameters
        ----------
        self: class
            class self.
        Return
        ------
        self: class
            class object with tread start.
        """
        Thread(target = self.get_frame, args=()).start()
        return self
    def get_frame(self):
        """
        method yiled frame from get_frame() method 
        after emotion detection.

        Parameters
        ----------
        None

        Return
        ------
        frame: bytes 
            return live streaming frame with emotion detection and 
            landmarks in bytes form.
        """
        while not self.stopped:
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_detect.detectMultiScale(gray, 1.3, 3)
            landmark_points_list = self.classifier.extract_landmark_points(img = self.frame)
            for x_axis, y_axis, width, height in faces:
                sub_face_img = gray[y_axis : y_axis + height, x_axis : x_axis + width]
                resized = cv2.resize(sub_face_img,(48,48))
                normalize = resized/255.0
                reshaped = np.reshape(normalize, (1, 48, 48, 1))
                result = self.model.predict(reshaped)
                label = np.argmax(result, axis=1)[0]
                for lm_points in landmark_points_list:
                    draw_landmark_points(points = lm_points, img = self.frame)
                print(label)
                cv2.rectangle(self.frame, (x_axis, y_axis),
                            (x_axis + width, y_axis + height), (0,0,255), 1)
                cv2.rectangle(self.frame, (x_axis, y_axis),
                            (x_axis + width, y_axis + height),(50,50,255),2)
                cv2.rectangle(self.frame, (x_axis, y_axis - 40),
                            (x_axis + width, y_axis),(50,50,255),-1)
                cv2.putText(self.frame, labels_dict[label], (x_axis, y_axis - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),2)
    def stop(self):
        """
        method stop the thread.

        Parameters
        ----------
        self

        Return
        ------
        None
        """
        self.stopped = True
