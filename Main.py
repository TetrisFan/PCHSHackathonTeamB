from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def run():
    return render_template('HomePage.html')


@app.route('/SearchFilter')
def filter():
    return render_template('FilterPage.html')


if __name__ == '__main__':
    app.run(config=True)
