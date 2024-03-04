from flask import Flask, request, jsonify
import socket
import json

app = Flask(__name__)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.route('/register', methods=['PUT'])
def register():
    content = request.json
    hostname = content['hostname']
    ip = content['ip']
    as_ip = content['as_ip']
    as_port = content['as_port']

    message = f"----\nTYPE=A\nNAME={hostname}\nVALUE=IP_ADDRESS\nTTL=10\n----"
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(message.encode(), (as_ip, int(as_port)))

    return jsonify({"message": "Registration successful"}), 201

@app.route('/fibonacci')
def fibonacci_service():
    number = request.args.get('number', default=1, type=int)
    try:
        # Calculate Fibonacci number
        result = fib(number)
        return jsonify({"fibonacci": result}), 200
    except ValueError:
        # If the provided number is not an integer
        return jsonify({"error": "Bad format"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
