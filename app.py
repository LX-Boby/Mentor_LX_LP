import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for, jsonify
from pymongo import MongoClient

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', title="Home")


@app.route('/about')
def about():
    return render_template('about.html', title="About")


@app.route('/mentors')
def mentors():
    return render_template('mentors.html', title="Mentors")


@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")


@app.route('/auth')
def auth():
    return render_template('auth.html', title="Authentication")


@app.route('/detail/<keyword>')
def detail(keyword):
    print(keyword)
    return render_template('detail.html', word=keyword)


@app.route('/api/save_word', methods=['POST'])
def save_word():
    return jsonify({
        'result': 'success',
        'msg': 'the word was saved',
    })


@app.route('/api/delete_word', methods=['POST'])
def delete_word():
    return jsonify({
        'result': 'success',
        'msg': 'the word was deleted',
    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
