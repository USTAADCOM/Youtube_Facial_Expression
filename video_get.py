"""
video_get module display frames using a dedicated thread.
"""
import time
from threading import Thread
import cv2
from cap_from_youtube import cap_from_youtube
class VideoGet:
    """
    Class that continuously gets frames from webcame or youtube video
    with a dedicated thread.

    Attributes
    ----------
    src : int
        cam index 0 for webcam.
    stream : ndarray
        frame get from youtube video or live cam.
    fps: float
        frame per second.
    Methods
    -------
    start():
        start the thread for CountsPerSec class.
    get(): 
        get and return the frame from selected source.
    stop():
        method to stop the thread.
    """
    def __init__(self, src=0):
        """
        Constructs all the necessary attributes for the VideoShow object.

        Parameters
        ----------
        src: int
            cam index 0 for webcam.
        stream : ndarray
            frame get from youtube video or live cam.
        frame_per_second: float
            frame per second.
        stopped: bool
            thread start or stop.
        """
        self.stream = cap_from_youtube(src, '360p')
        self.stream.set(cv2.CAP_PROP_FPS, 2)
        self.frame_per_second = 1/30
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
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
        Thread(target=self.get, args=()).start()
        return self
    def get(self):
        """
        Doc String
        """
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
            time.sleep(self.frame_per_second)
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
