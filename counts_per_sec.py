"""
counts_per_sec module refresh frame after each second and count frame per second
rate.
"""
from datetime import datetime
class CountsPerSec:
    """
    Class that tracks the number of occurrences ("counts") of an arbitrary event 
    and returns the frequency in occurrences (counts) per second.

    Attributes
    ----------
    _start_time : str
        first name of the person
    _num_occurrences : int
        count for the number of per second frames.

    Methods
    -------
    start():
        start the thread for CountsPerSec class.
    increment(): 
        increment the counts after each second CountsPerSec class.
    counts_per_sec():
        return total counts per second frames.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the CountsPerSec object.

        Parameters
        ----------
        None
        """
        self._start_time = None
        self._num_occurrences = 0
    def start(self):
        """
        start method start the thread for CountsPerSec class.

        Parameters
        ----------
        self
            CountsPerSec object.
        
        Return
        ------
        self
            CountsPerSec object.
        """
        self._start_time = datetime.now()
        return self
    def increment(self):
        """
        increment method increment the counts after each second CountsPerSec class.

        Parameters
        ----------
        self
            CountsPerSec object.
        
        Return
        ------
        _num_occurrences: int
            CountsPerSec counter variable.
        """
        self._num_occurrences += 1
    def countsPerSec(self):
        """
        counts_per_sec method return total counts per second frames.

        Parameters
        ----------
        self
            CountsPerSec object.
        
        Return
        ------
            total counts per second frames.
        """
        elapsed_time = (datetime.now() - self._start_time).total_seconds()
        return self._num_occurrences / elapsed_time if elapsed_time > 0 else 0
