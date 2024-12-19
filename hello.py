import socket
from datetime import datetime
from flask import Flask

app = Flask(__name__)

server_start_time = datetime.now()

@app.route('/')
def hello_world():
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
</head>
<body>
    <h1>Hello, World - MIKE IS HAVING COFFEE!</h1>
    <p>Server started at: { server_start_time }</p>
    <p>Page last rendered at: { datetime.now() }</p>
</body>
</html>
'''

if __name__ == '__main__':
    # Dynamically fetch the local IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    # Log the IP address
    print(f" * Local IP address: http://{local_ip}:5000")
    print(f" * Flask server started at {server_start_time}")

    # Run the Flask server
    app.run(host='0.0.0.0', port=5000, debug=True)