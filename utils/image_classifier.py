"""
Model will take the image as nd array and return the list of all the images.  
"""
import numpy as np
from utils.data_land_marker import LandMarker
class ImageClassifier:
    """
    string
    """
    def __init__(self, land_marker: LandMarker)-> None:
        self.land_marker = land_marker

    def extract_landmark_points(self, img: np.ndarray)-> list:
        """
        extract_landmark_points method take images nd array as input
        and return the list of all the images with landmark on each face.

        Parameters
        ----------
        img: ndarray

        Return
        ------
        List
            list of all the images with landmark on each face.
        """
        return self.land_marker.img_to_landmark_points(img)
