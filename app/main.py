from flask import Flask, request, jsonify, render_template
from kms_utils import encrypt_password, decrypt_password
import pymysql
import os

app = Flask(__name__, template_folder="templates")

# Database connection
db = pymysql.connect(
    host=os.environ['DB_HOST'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASS'],
    database=os.environ['DB_NAME']
)

# Home route to serve frontend
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to register user
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    encrypted_pw = encrypt_password(data['password'])
    with db.cursor() as cur:
        cur.execute(
            "INSERT INTO users (username, encrypted_password) VALUES (%s, %s)",
            (data['username'], encrypted_pw)
        )
        db.commit()
    return jsonify({"message": "User registered"})

# API endpoint to login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    with db.cursor() as cur:
        cur.execute("SELECT encrypted_password FROM users WHERE username=%s", (data['username'],))
        row = cur.fetchone()
        if row:
            decrypted_pw = decrypt_password(row[0])
            if decrypted_pw == data['password']:
                return jsonify({"message": "Login success"})
    return jsonify({"message": "Login failed"}), 401

if __name__ == '__main__':
    app.run(debug=True)