from datetime import date
from flask import Flask, render_template, request
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

@app.route('/post')
def jobPostPage():
    return render_template('JobPosting.html')


@app.route('/postJob', methods = ['POST'])
def postJob():
    json = request.get_json()
    jobInfo, visaType = json['dummyJob'], json['visa']
    dateInfo = jobInfo['postDate']
    jobInfo['postDate'] = "'" + str(dateInfo['year']) + "-" + str(dateInfo['month'])
    jobInfo['postDate'] += "-" + str(dateInfo['day']) + "'"
    jobKeys = ('postDate', 'title', 'description', 'address', 'company')
    for key in jobKeys[1:]:
        jobInfo[key] = '"' + jobInfo[key] + '"'
    jobInfo = (',').join([jobInfo[key] for key in jobKeys])
    conn = sql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Job (siteName) VALUES (\"dummySite\")")
    cursor.fetchall()
    cursor.execute("SELECT MAX(id) AS id FROM Job")
    id = cursor.fetchall()[0][0]
    cursor.execute('INSERT INTO JobVisa (visaType, jobId) VALUES ("' + visaType + '", ' + str(id) + ")")
    cursor.execute('''INSERT INTO
        Dummy (jobId, postDate, title, description, address, company)
        VALUES (''' + str(id) + ", " + jobInfo + ');')
    conn.commit()
    return "success"


if __name__ == '__main__':
    app.run(debug=True)
