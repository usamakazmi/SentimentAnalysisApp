from flask import Flask, render_template, json,url_for, request, redirect
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)
#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')


    
if __name__ == "__main__":
    app.run(debug=True)