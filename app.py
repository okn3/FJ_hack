#coding:utf-8
import sys
from flask import Flask
from flask import render_template
sys.path.append('module')
from analize import answer_msg
import output_file
app = Flask(__name__)

# トップページ
@app.route('/')
def show_top():
    return render_template("top.html")

# 結果ページ
@app.route('/result')
def result():
    # 分析処理を挟む
    output_file.create("結果ファイル")
    return render_template("result.html")


# flask動作検証用

@app.route('/top/<msg>')
def test_msg(msg):
    return render_template("top.html",msg=msg)

@app.route('/module_test')
def module_test():
    return answer_msg()

if __name__ == '__main__':
    app.run(debug=True)

