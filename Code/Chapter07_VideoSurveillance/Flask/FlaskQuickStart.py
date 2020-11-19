# Chương trình làm quen với flask, output video stream capture từ
# camera lên web server
# Chay chuong trinh
# win 10: Mở Anaconda shell, gõ cmd: py FlaskQuickStart.py

import cv2
from flask import Response
from flask import render_template
from flask import Flask, url_for
from markupsafe import escape
app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


cap = cv2.VideoCapture(0)
@app.route('/video_stream')
def video_stream():
    def generate():
        while True:
            # frame = cv2.imread("static/TwoFaces.jpg")
            ret, frame = cap.read()
            ret, jpeg = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
    return Response(generate(),  mimetype='multipart/x-mixed-replace; boundary=frame')


app.run(host="0.0.0.0", port=5000, debug=True,
        threaded=True, use_reloader=False)
