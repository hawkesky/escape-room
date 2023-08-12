import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/vault')
def vault():
    return render_template('vault.html', secret_code=os.getenv("SECRET_CODE"))


@app.route('/authenticate', methods=['GET', 'POST'])
def authenticate():
    if request.method == 'POST':
        # Sprawdź odpowiedzi na pytania (case insensitive)
        answers = {
            'author_robot_fables': 'stanisław lem',
            'david_bowie_song': 'space oddity',
            'anakin_skywalker_mother': 'shmi'
        }

        user_answers = {
            'author_robot_fables': request.form['author_robot_fables'].lower(),
            'david_bowie_song': request.form['david_bowie_song'].lower(),
            'anakin_skywalker_mother': request.form['anakin_skywalker_mother'].lower()
        }

        if user_answers == answers:
            return redirect(url_for('vault'))

    return render_template('authenticate.html')


if __name__ == '__main__':
    if os.getenv("ENV") == "local":
        app.run(debug=True)
    else:
        app.run(debug=False)

