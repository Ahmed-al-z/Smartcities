from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images')

@app.route('/')
def index():
    images = sorted(os.listdir(IMAGE_FOLDER), reverse=True)
    return render_template('index.html', images=images)

@app.route('/images/<filename>')
def image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
