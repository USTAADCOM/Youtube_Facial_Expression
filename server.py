"""
Emotion detection application flask server main page.
"""
from flask import (
    Flask, render_template,
    Response, request
    )
from main_thread import main_thread
import cv2

app = Flask(__name__)

def put_iterations_per_sec(frame, iterations_per_sec):
    """
    Add iterations per second text to lower-left corner of a frame.

    Parameters
    ----------
    frame: ndarray
        video frame with ndarray.
    iterations_per_sec: method
        class CountPerSec method count frome iterations per second.
    """
    cv2.putText(frame, "{:.0f}".format(iterations_per_sec),
        (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
    return frame

def gen_frames(video_getter, video_classifier, count_p_second)-> bytes:
    """
    method yiled frame from get_frame() method 
    after emotion detection.

    Parameters
    ----------
    None

    Return
    ------
    frame: yiled
        yield live streaming frame with emotion detection and 
        landmarks.
    """
    while True:
        if video_getter.stopped:
            video_getter.stop()
            break
        frame = video_getter.frame
        video_classifier.frame = frame
        text_frame = put_iterations_per_sec(video_classifier.frame,
                                            count_p_second.countsPerSec())
        # video_shower.frame = text_frame
        count_p_second.increment()
        _, jpeg = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

def get_form_data(request_var)-> str:
    """
    method will take the data from the form and after extracting return 
    the data.
    Parameters:
    ----------
    request_var: Request
        request send by the user from welcome.html page.
    Return:
    ------
    url: string
        return the data send by the user.

    """
    url = request_var.form.get('url')
    return url

@app.route('/')
def index():
    """
    Index page emotion detcetion vide streaming application.
    
    Parameters
    ----------
    None

    Return
    ------
        render template index.html.
    """
    return render_template('welcome.html')

@app.route('/video_feed', methods = ['POST'])
def video_feed():
    """
    method return response of yiled frame from gen_frames() method 
    after emotion detection.

    Parameters
    ----------
    None

    Return
    ------
    frame: Response
        return live streaming frame with emotion detection and 
        landmarks.
    """
    video_url = get_form_data(request)
    video_getter, video_classifier, count_p_second = main_thread(video_url)
    return Response(gen_frames(video_getter, video_classifier,
                               count_p_second),
                     mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
