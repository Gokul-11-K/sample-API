from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gotamil",
    database="myapp"
)

cursor = db.cursor()

# API 1: Save text to MySQL
@app.route('/save', methods=['POST'])
def save_text():
    data = request.get_json()
    content = data.get('content', '').strip()

    if not content:
        return jsonify({"message": "Please enter some text"}), 400

    sql = "INSERT INTO messages (content) VALUES (%s)"
    cursor.execute(sql, (content,))
    db.commit()

    return jsonify({"message": "Text saved successfully!"})

# API 2: Get saved text from MySQL
@app.route('/messages', methods=['GET'])
def get_messages():
    cursor.execute("SELECT * FROM messages")
    rows = cursor.fetchall()

    messages = [
        {"id": row[0], "content": row[1]}
        for row in rows
    ]

    return jsonify(messages)

# Start the server
if __name__ == '__main__':
    app.run(debug=True)