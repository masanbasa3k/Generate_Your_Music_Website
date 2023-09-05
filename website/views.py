from .model.model_file import create_music

from flask import Blueprint, render_template, request, send_file, redirect, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/generate_music', methods=['POST'])
def generate_music():
    create_music()
    return redirect(url_for('views.home'))

@views.route('/download_music')
def download_music():
    return send_file('static/music.mid')


