import os
import time
import mysql.connector
from flask import Flask,render_template,request

FLAG = 'DH{**flag**}'

app = Flask(__name__)

MYSQL_HOST=os.environ.get('MYSQL_HOST')
MYSQL_USER=os.environ.get('MYSQL_USER')
MYSQL_PASSWORD=os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE=os.environ.get('MYSQL_DATABASE')

def db_connection():
    for _ in range(0,100,1):
        try:
           conn=mysql.connector.connect(host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PASSWORD,database=MYSQL_DATABASE) 
           return conn
        except:
            time.sleep(5)   
    return None
            
connection=db_connection()

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/login",methods=['POST'])
def login():
    banned_word=['or', 'and', 'from', 'where', 'insert', 'update', 'delete', 'join', 'substr', 'table', 'database', 'schema', 'if', 'order', 'group', 'by', 'as', 'limit', 'offset', 'exists', 'between', 'regexp', 'binary', 'file', 'not', 'rlike', 'left', 'right', 'mid', 'lpad', 'rpad', 'char', 'user', 'version', 'session', 'sleep', 'benchmark', 'hex', 'base64', '0b', '0x']
    banned_letter='()[]+-*/=:;"<>.?!&|\\$%^~`'
    username=request.form.get('username')
    password=request.form.get('password')
    for word in banned_word:
        if (word in username.lower()) or (word in password.lower()):
            return render_template('index.html',message='No Hack~ ^_^')
    for i in range(0,len(banned_letter),1):
        letter=banned_letter[i]
        if (letter in username.lower()) or (letter in password.lower()):
            return render_template('index.html',message='No Hack~ ^_^')
    query=f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    user=None
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        user=cursor.fetchone()
        cursor.close()
    except:
        user=None
    finally:
        if user and user[1]=='Rootsquare':
            return render_template('login.html',username=user[1],success=FLAG)
        elif user:
            return render_template('login.html',username=user[1],success='')
        else:
            return render_template('index.html',message='Invalid User ID or Password.')

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)