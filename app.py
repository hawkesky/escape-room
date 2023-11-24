import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/check_keyword', methods=['POST'])
def check_keyword():
    keyword = request.form['keyword']
    user_agent = request.headers.get('User-Agent')
    if keyword.lower() == 'apokalipsa':
        if "iPhone" in user_agent:
            return redirect('https://apps.apple.com/us/app/reverse-audio/id1254981556')
        else:
            return redirect('https://play.google.com/store/apps/details?id=pl.ayground.playbackapp&hl=pl&gl=US')
    else:
        return render_template('index.html', message='Nieprawidłowa odpowiedź!')


if __name__ == '__main__':
    if os.getenv("ENV") == "local":
        app.run(debug=True)
    else:
        app.run(debug=False)

