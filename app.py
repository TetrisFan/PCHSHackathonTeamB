from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_DB'] = 'WorkVisaJobSearch'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'koolkid96'

sql = MySQL(app)
sql.init_app(app)

@app.route('/')
def run():
    return render_template('HomePage.html')


@app.route('/search')
def filter():
    return render_template('FilterPage.html')


@app.route('/postJob', methods = ['POST'])
def postJob():
    cursor = sql.connect().cursor()
    cursor.execute("SELECT postDate FROM Dummy")
    dates = [row[0] for row in cursor.fetchall()]
    return str(dates) + str(type(dates[0]))


if __name__ == '__main__':
    app.run(debug=True)
