from flask import Flask, request, render_template, redirect, url_for, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(
    'mongodb://lx-boby:bobyhard@ac-llkguct-shard-00-00.rmswowm.mongodb.net:27017,ac-llkguct-shard-00-01.rmswowm.mongodb.net:27017,ac-llkguct-shard-00-02.rmswowm.mongodb.net:27017/?ssl=true&replicaSet=atlas-spa6pr-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.db_lx_pkl1


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
    return render_template('auth.html', title="User")


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
