from db.querries import get_data
from flask import Flask, app, request, jsonify

app = Flask(__name__)

@app.route('/set/item', methods=['POST'])
def add_item():
    item = request.get_json()

    response = {
        'status': 'success',
        'received_item': item
    }

    return jsonify(response), 200


if __name__=="__main__":
    app.run()

