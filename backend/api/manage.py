from flask import Flask, jsonify
import sqlite3
from settings import DB_NAME
import psycopg2
app = Flask(__name__)

app.config.from_mapping(
    DATABASE= DB_NAME
)

@app.route('/movies')
def movies():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute('select * from movies;')
    movie_records = cursor.fetchall()
    return jsonify(movie_records)