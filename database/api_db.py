from flask import Flask, jsonify, request
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)


@app.route('/yolo/list', methods=['GET'])
def list_objects():
    objs = database.select_db()
    return jsonify(objs)


@app.route('/yolo/save', methods=['POST'])
def save_objects():
    response = request.json
    title = response['title']
    img = response['image_result']
    objects = response['objects']
    database.insert_db(title, objects, img)
    return jsonify({'response': 'record inserted'})


if __name__ == '__main__':
    app.run(debug=True)