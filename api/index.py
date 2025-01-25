from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from your API!", "status": "success"})

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "data": [
            {"id": 1, "name": "Item 1"},
            {"id": 2, "name": "Item 2"},
            {"id": 3, "name": "Item 3"}
        ],
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)
