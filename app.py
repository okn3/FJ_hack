#coding:utf-8
import sys
from flask import Flask
from flask import render_template
sys.path.append('module')

from analize import answer_msg 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/top')
def show_top():
    return render_template("top.html")

@app.route('/top/<msg>')
def test_msg(msg):
    return render_template("top.html",msg=msg)

@app.route('/module_test')
def module_test():
    return answer_msg()

if __name__ == '__main__':
    app.run(debug=True)

