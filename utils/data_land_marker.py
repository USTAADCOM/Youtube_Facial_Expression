"""
take the nd array of images from a from and return perform landmark activities 
over the faces.
"""
import dlib
import numpy as np
LAND_MARK_POINTS_SIZE = 68
def shape_to_np(shape, size: int):
    """
    method face shape and landmarks count as input and arrary with
    x axis and y axis landmarks as input.

    Parameters
    ----------
    shape
        face shape on frame.
    size: int
        size of the Landmark points which is 68 in dlib.

    Return
    ------
        ndarray of faces on a frame.
    """
    return np.asarray([(shape.part(i).x, shape.part(i).y) for i in range(0, size)])

class LandMarker:
    """
    Class that continuously gets frames from webcame or youtube video
    extract faces from faces and return faces with landmarks.

    Attributes
    ----------
    landmark_predictor_path : str
        model to predict the face landmark.
    predictor: object
        dlib shape predictor.
    detector: object
        dlib frame or image faces detector.
    Methods
    -------
    img_to_landmark_points():
        take image as array and return the list of the landmaek points 
        in a image frame.
    """
    def __init__(self, landmark_predictor_path: str):
        """
        Constructs all the necessary attributes for the LandMarker object.

        Parameters
        ----------
        landmark_predictor_path : str
            model to predict the face landmark.
        predictor: object
            dlib shape predictor.
        detector: object
            dlib frame or image faces detector.
        """
        self.predictor = dlib.shape_predictor(landmark_predictor_path)
        self.detector = dlib.get_frontal_face_detector()
    def img_to_landmark_points(self, img: np.ndarray)-> list:
        """
        method take image as array and return the list of the landmaek points 
        in a image frame.

        Parameters
        ----------
        img: ndarray
            ndarray of images in video frame.
        
        Retrun
        ------
            list of all the images with landmark on each face.
        """
        detections = self.detector(img, 1)
        if len(detections) < 1:
            return [None]
        landmark_points_list = []
        for (_, rect) in enumerate(detections):
            shape = self.predictor(img, rect)
            landmark_points_list.append(shape_to_np(shape, size = LAND_MARK_POINTS_SIZE))
        return landmark_points_list
