from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)

@web_site.route('/')
def login():
	return render_template('login.html')

@web_site.route('/')
def main():
	return render_template('index.html')

@staticmethod
def insert_record(doc):
    Database.DB.Database.insert_one({"user_chat"})

web_site.run(host='0.0.0.0', port=8080)
