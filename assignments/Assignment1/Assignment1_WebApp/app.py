from flask import Flask, render_template, request, redirect, url_for
import os
import cv2 as cv
from werkzeug.utils import secure_filename

import image_processor

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Open the uploaded image
        image = cv.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resized = image_processor.resize_image_512(image, filename)
        rgb = image_processor.bgr2rgb(resized, filename)
        gray = image_processor.rgb2gray(rgb, filename)
        rgb_split_channels = image_processor.split_rgb_channels(rgb, filename)
        average_blur = image_processor.average_blur(rgb, filename)
        gaussian_blur = image_processor.gaussian_blur(rgb, filename)
        detect_edges = image_processor.detect_edges(rgb, filename)
        # cv.imwrite(os.path.join(app.config['UPLOAD_FOLDER'], "split_rgb_channels_" + filename), rgb_split_channels)
        return redirect(url_for('result', filename=filename))
    return render_template('upload.html')

@app.route('/result/<filename>')
def result(filename):
    return render_template("result.html", filename=filename)

@app.route('/view/rgb/<filename>')
def view_image(filename):
    filename = "rgb_" + filename
    return '<h3>RGB Image:</h3> \n<img src="' + \
        url_for('static', filename='uploads/' + filename) + '">'

@app.route('/view/gray_scale/<filename>')
def view_gray(filename):
    filename = "gray_" + filename
    return '<h3>Gray Scale Image:</h3> \n<img src="' + \
        url_for('static', filename='uploads/' + filename) + '">'

@app.route("/view/split_rgb_channels/<filename>")
def view_rgb_split_channels(filename):
    filename = "split_rgb_channels_" + filename
    return '<h3>RGB Channels Image [Split]:</h3> \n<img src="' + \
        url_for('static', filename='uploads/' + filename) + '">'

@app.route("/view/average_blur/<filename>")
def average_blur(filename):
    filename = "average_blur_" + filename
    return '<h3>Average Blur Filters [Box Mask]:</h3> \n<img src="' + \
        url_for('static', filename='uploads/' + filename) + '">'

@app.route("/view/gaussian_blur/<filename>")
def gaussian_blur(filename):
    filename = "gaussian_blur_" + filename
    return '<h3>Gaussian Blur Filters:</h3> \n<img src="' + \
        url_for('static', filename='uploads/' + filename) + '">'

@app.route("/view/detect_edges/<filename>")
def detect_edges(filename):
    filename = "detect_edges_" + filename
    return '<h3>Detect Edges:</h3> \n<img src="' + \
        url_for('static', filename='uploads/' + filename) + '">'

if __name__ == '__main__':
    app.run(debug=True)
