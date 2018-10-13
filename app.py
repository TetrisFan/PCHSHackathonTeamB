from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def run():
    return render_template('HomePage.html')


@app.route('/search')
def filter():
    return render_template('FilterPage.html')

@app.route('/postJob', methods = ['POST'])
def postJob():
    json = request.get_json()
    return str(type(json))


if __name__ == '__main__':
    app.run(debug=True)
