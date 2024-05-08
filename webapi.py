from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/post_example', methods=['POST'])
def post_example():
    data = request.get_json()  # 获取POST请求中的JSON数据
    if data:
        name = data.get('name')  # 假设JSON数据中有一个名为'name'的字段
        return jsonify({'message': f'Hello, {name}! Received your POST request.'})
    else:
        return jsonify({'error': 'No JSON data received in the request.'}), 400
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})


if __name__ == '__main__':
    app.run(debug=True)
