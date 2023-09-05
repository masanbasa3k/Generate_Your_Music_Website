from flask import Flask
from os import path

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your secret key'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app

'''from website.model.model_file import create_music

from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_music', methods=['POST'])
def generate_music():
    # Müzik oluştur
    create_music()
    return "Music is generated!"

@app.route('/download_music')
def download_music():
    # Müziği çal
    return send_file('static/music.mid')

if __name__ == '__main__':
    app.run(debug=True)'''