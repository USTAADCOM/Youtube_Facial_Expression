"""
video_show module display frames using a dedicated thread.
"""
import time
from threading import Thread
import cv2

class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.

    Attributes
    ----------
    frame : ndarray
        frame return by the detection module.
    stopped : bool
        thread start or stop check.
    fps: float
        frame per second.
    Methods
    -------
    start():
        start the thread for CountsPerSec class.
    show(): 
        display frames after emotion detection.
    stop():
        method to stop the thread.
    """
    def __init__(self, frame=None):
        """
        Constructs all the necessary attributes for the VideoShow object.

        Parameters
        ----------
        frame: ndarray
            frame from webcam, picture or youtube video.
        """
        self.frame = frame
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
        Thread(target = self.show, args=()).start()
        return self
    def show(self):
        """
        Doc string
        """
        while not self.stopped:
            cv2.imshow("Video", self.frame)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True
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
