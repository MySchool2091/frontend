# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session,jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os
import socket
import mysql.connector
# Production
#from gevent.pywsgi import WSGIServer

app = Flask(__name__)


#Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'
#--------------------------------------------------------------------------
#MySQL Local
'''
app.config['MYSQL_HOST'] ='192.168.137.128'
app.config['MYSQL_USER'] = 'srejoy'
app.config['MYSQL_PASSWORD'] = 'xyz'
app.config['MYSQL_DB'] = 'mrpskp'
'''
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
#MySQL RDS on AWS
#'''
app.config['MYSQL_HOST'] = os.getenv("MYSQL_SERVICE_HOST") 
app.config['MYSQL_USER'] = os.getenv("MYSQL_DB_USER") 
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_DB_PASSWORD") #'admin'
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")  #'MRPSKP'
app.config["MYSQL_DATABASE_PORT"] = os.getenv("MYSQL_SERVICE_PORT") #3306 #os.getenv("MYSQL_SERVICE_PORT")
#'''
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
#MySQL Docker
'''
app.config['MYSQL_HOST'] = os.getenv("MYSQL_SERVICE_HOST")  #'mysql-service'
app.config['MYSQL_USER'] = os.getenv("MYSQL_DB_USER") #'admin'
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_DB_PASSWORD") #'admin'
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")  #'MRPSKP'
app.config["MYSQL_DATABASE_PORT"] = os.getenv("MYSQL_SERVICE_PORT") #3306 #os.getenv("MYSQL_SERVICE_PORT")
'''
#--------------------------------------------------------------------------


mysql = MySQL(app)

@app.route('/student')
def home():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM students')
    students =cursor.fetchall()
    return render_template('index.html', students=students)

@app.route('/student_add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':

            fname = request.form['fname'],
            lname = request.form['lname'],
            Gender = request.form['Gender'],
            ID = request.form['ID'],
            Subject = request.form['Subject'],
            phone = request.form['phone'],
            AdminDate = request.form['AdminDate']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            sql = "INSERT INTO students " \
             "VALUES (% s, % s, % s, % s, % s, % s, % s)"
            cursor.execute(sql, (fname,lname,Gender,ID,Subject,phone,AdminDate,))
            mysql.connection.commit()
    return redirect(url_for('home'))


@app.route('/student_delete_student/<ID>', methods=['GET'])
def delete_student(ID):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "DELETE FROM students  WHERE ID= %s"
    val = (ID,)
    cursor.execute(sql,val)
    mysql.connection.commit()
    return redirect(url_for('home'))
'''
@app.route('/show_student/<ID>', methods=['GET'])
def show_student(ID):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "SELECT * FROM students  WHERE ID= %s"
    val = (ID,)
    cursor.execute(sql,val)
    student =cursor.fetchone()
    return render_template('index_one.html', student=student)
    #return redirect(url_for('home'))
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=3007)


'''
 app.run(host='0.0.0.0', debug=False,port=3000)
'''