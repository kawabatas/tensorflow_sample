#!/usr/bin/python3
import os
from flask import Flask, render_template, request, send_from_directory
from recognizer import Recognizer

app = Flask(__name__)
app.recognizer = Recognizer()

if __name__ == '__main__':
    file_name = 'target.jpg'
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    result = app.recognizer.run(file_path)
