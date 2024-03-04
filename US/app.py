from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fibonacci')
def fibonacci():
    # Extract parameters from the request
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    # Validate the parameters
    if not all([hostname, fs_port, number, as_ip, as_port]):
        return jsonify({"error": "Missing parameters"}), 400
    result = number

    # Return the result
    return jsonify({"hostname": hostname, "fs_port": fs_port, "number": number, "as_ip": as_ip, "as_port": as_port, "result": result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
