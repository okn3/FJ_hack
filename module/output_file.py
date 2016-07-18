#coding:utf-8
import os

def create(text):
    f = open("static/sample.txt","w") #新規作成
    f.write(text)
    f.close()


if __name__ == "__main__":
    create("書き込み完了")
