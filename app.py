import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/check_keyword', methods=['POST'])
def check_keyword():
    k = request
    keyword = request.form['keyword']

    if keyword.lower() == 'apokalipsa':
        return redirect('https://mp3cut.net/pl/reverse-audio')
    else:
        return render_template('index.html', message='Nieprawidłowa odpowiedź!')


if __name__ == '__main__':
    if os.getenv("ENV") == "local":
        app.run(debug=True)
    else:
        app.run(debug=False)

